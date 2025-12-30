rm -rf terraform-provider-aws
git clone -n --depth=1 --filter=tree:0 \
	https://github.com/hashicorp/terraform-provider-aws.git
cd terraform-provider-aws
git sparse-checkout set --no-cone website/docs/r names/data
git checkout
rm -rf .git