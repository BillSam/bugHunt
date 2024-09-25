#!/bin/bash
domain=$1
for ns in $(host -t NS $domain | cut -d " " -f4); do
    host -l $domain $ns | grep "has address"
done