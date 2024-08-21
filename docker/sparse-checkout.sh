git clone -n --depth=1 --filter=tree:0 -b python \
	https://github.com/aws-samples/aws2tf.git aws2tf-py
cd aws2tf
git sparse-checkout set --no-cone .python/docker docker
git checkout
rm -rf .git