#!/usr/local/bin/zsh

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Undoing any AWS credentials in ENV${NC} "

unset AWS_PROFILE
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
unset AWS_REGION
unset AWS_DEFAULT_REGION
