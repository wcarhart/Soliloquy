if [[ "$TRAVIS_EVENT_TYPE" == "pull_request" ]] ; then
	if [[ "$TRAVIS_PULL_REQUEST_BRANCH" == "master" ]] ; then
		echo "prod-deploy"
	else
		echo "dev-test"
		echo "dev-deploy"
	fi
fi
