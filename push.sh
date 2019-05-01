#!/usr/bin/env bash
git add .
git commit -m $1
git push -u origin master
git push -u hub master
open https://github.com/yangjh2019
open https://gitee.com/yangjh
