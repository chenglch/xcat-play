export XCAT3_URL=http://{{ xcat3_api_ip_address }}:{{ xcat3_api_port }}
# TODO(chenglch):this should be put in the role of controller
alias xcat3-copycds="pypy {{pypy_bin}}/xcat3-copycds"