# git filter-branch -f --env-filter '
# OLD_EMAIL="sasa0309sho@gmail.com"
# CORRECT_NAME="aerosmooth"
# CORRECT_EMAIL="sasa0309sho@gmail.com"
#
# if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
# then
#     export GIT_COMMITTER_NAME="$CORRECT_NAME"
#     export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
# fi
# if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
# then
#     export GIT_AUTHOR_NAME="$CORRECT_NAME"
#     export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
# fi
# ' --tag-name-filter cat -- --branches --tags
git filter-branch --env-filter '

OLD_NAME="sasa0309sho-blip"
NEW_NAME="aerosmooth"

if [ "$GIT_AUTHOR_NAME" = "$OLD_NAME" ]; then
    export GIT_AUTHOR_NAME="$NEW_NAME"
fi

if [ "$GIT_COMMITTER_NAME" = "$OLD_NAME" ]; then
    export GIT_COMMITTER_NAME="$NEW_NAME"
fi
' --tag-name-filter cat -- --branches --tags
