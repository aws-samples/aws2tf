"""
aws2tf manifest module — writes aws2tf.json to track execution progress.

The manifest enables --resume from any interruption point by recording:
- Which stage was last completed successfully
- Workspace path, account, region
- Command-line arguments used
- Resource counts at each stage
- Timestamps and durations
"""

import json
import os
import glob
import datetime
import logging

log = logging.getLogger('aws2tf')

# Module-level manifest state
_manifest = None
_manifest_path = None


def _now_iso():
    return datetime.datetime.now().isoformat(timespec='seconds')


def init(workspace_path, account, region, command_args):
    """
    Initialize a new manifest at the start of an aws2tf run.
    
    Args:
        workspace_path: The generated/tf-* directory path
        account: AWS account ID
        region: AWS region
        command_args: Parsed argparse namespace
    """
    global _manifest, _manifest_path
    
    # Write to current directory (we're already chdir'd into the workspace)
    _manifest_path = "aws2tf.json"
    
    _manifest = {
        "version": "1.0",
        "started_at": _now_iso(),
        "status": "in_progress",
        "workspace": {
            "path": workspace_path,
            "account": account,
            "region": region
        },
        "command": {
            "type": getattr(command_args, 'type', None),
            "id": getattr(command_args, 'id', None),
            "flags": {
                "fast": getattr(command_args, 'fast', False),
                "merge": getattr(command_args, 'merge', False),
                "debug": getattr(command_args, 'debug', False),
                "validate": getattr(command_args, 'validate', False),
                "accept": getattr(command_args, 'accept', False),
                "singlefile": getattr(command_args, 'singlefile', False),
                "serverless": getattr(command_args, 'serverless', False),
            }
        },
        "current_stage": 1,
        "last_completed_stage": 0,
        "stages": {},
        "resource_counts": {},
        "errors": [],
        "completed_at": None
    }
    
    _write()


def load(workspace_path):
    """
    Load an existing manifest from a workspace directory.
    
    Args:
        workspace_path: Path to the generated/tf-* directory (unused, reads from cwd)
        
    Returns:
        dict: The loaded manifest, or None if not found
    """
    global _manifest, _manifest_path
    
    # We're already chdir'd into the workspace
    _manifest_path = "aws2tf.json"
    
    if not os.path.isfile(_manifest_path):
        return None
    
    try:
        with open(_manifest_path, 'r') as f:
            _manifest = json.load(f)
        return _manifest
    except (json.JSONDecodeError, IOError) as e:
        log.warning("Could not load manifest: %s", e)
        return None


def stage_start(stage_num, stage_name):
    """
    Record the start of a stage.
    
    Args:
        stage_num: Stage number (1-10)
        stage_name: Human-readable stage name
    """
    if _manifest is None:
        return
    
    key = f"stage_{stage_num}"
    _manifest["current_stage"] = stage_num
    _manifest["stages"][key] = {
        "name": stage_name,
        "status": "in_progress",
        "started_at": _now_iso(),
        "completed_at": None
    }
    _write()


def stage_complete(stage_num, extra_data=None):
    """
    Record successful completion of a stage.
    
    Args:
        stage_num: Stage number (1-10)
        extra_data: Optional dict of stage-specific metrics
    """
    if _manifest is None:
        return
    
    key = f"stage_{stage_num}"
    if key in _manifest["stages"]:
        _manifest["stages"][key]["status"] = "passed"
        _manifest["stages"][key]["completed_at"] = _now_iso()
        if extra_data:
            _manifest["stages"][key].update(extra_data)
    
    _manifest["last_completed_stage"] = stage_num
    _write()


def stage_failed(stage_num, error_message):
    """
    Record a stage failure.
    
    Args:
        stage_num: Stage number (1-10)
        error_message: Description of what went wrong
    """
    if _manifest is None:
        return
    
    key = f"stage_{stage_num}"
    if key in _manifest["stages"]:
        _manifest["stages"][key]["status"] = "failed"
        _manifest["stages"][key]["completed_at"] = _now_iso()
        _manifest["stages"][key]["error"] = error_message
    
    _manifest["status"] = "failed"
    _manifest["errors"].append({
        "stage": stage_num,
        "message": error_message,
        "timestamp": _now_iso()
    })
    _write()


def update_resource_counts(**counts):
    """
    Update resource count metrics in the manifest.
    
    Example:
        update_resource_counts(import_files=100, aws_files=100, state_resources=100)
    """
    if _manifest is None:
        return
    
    _manifest["resource_counts"].update(counts)
    _write()


def complete(success=True):
    """
    Mark the entire run as complete.
    
    Args:
        success: Whether the run completed successfully
    """
    if _manifest is None:
        return
    
    _manifest["status"] = "completed" if success else "failed"
    _manifest["completed_at"] = _now_iso()
    _write()


def get_last_completed_stage():
    """
    Return the last successfully completed stage number.
    
    Returns:
        int: Stage number (0 if nothing completed)
    """
    if _manifest is None:
        return 0
    return _manifest.get("last_completed_stage", 0)


def get_manifest():
    """Return the current manifest dict (or None)."""
    return _manifest


def _write():
    """Write manifest to disk."""
    if _manifest is None or _manifest_path is None:
        return
    
    try:
        with open(_manifest_path, 'w') as f:
            json.dump(_manifest, f, indent=2, default=str)
    except IOError as e:
        log.warning("Could not write manifest: %s", e)
