awk 'match($0, /^__v.*"(.*)"$/, a) {print a[1]}' __init__.py

