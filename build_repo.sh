#!/bin/sh

for dir in nodejs-*/; do
  cd $dir
  tito build --srpm --test --builder tito.builder.MockBuilder --arg mock_config_dir=mock/ --arg mock=el7-scl
  cd ../
done

# Notice el7-scl here is /etc/mock/el7-scl.cfg , copy it from this repo
mockchain -r el7-scl --tmp_prefix tfm --recurse /tmp/tito/*.src.rpm

# Remember to just run mockchain -l /var/tmp/mock-chain-tfm-28704-3a61j_hz/results/el7-scl/ to
# avoid 'recurse' building everything all the time
