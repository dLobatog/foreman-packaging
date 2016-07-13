#!/bin/sh

for dir in */; do
  cd $dir
  tito build --srpm --test --builder tito.builder.MockBuilder --arg mock_config_dir=mock/ --arg mock=el7-scl
  cd ../
done

mockchain -r el7-scl --tmp_prefix tfm --recurse /tmp/tito/*.src.rpm
