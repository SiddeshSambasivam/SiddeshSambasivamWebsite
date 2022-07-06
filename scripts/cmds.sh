create_post() {
    # Creates a new post in the blog directory
    read -p "Enter title: " title
    hugo new  --kind post blog/$title  
}

create_course() {
    read -p "Enter course title: " title
    hugo new --kind course courses/$title
}


if declare -f "$1" > /dev/null
then
  # call arguments verbatim
  "$@"
else
  # Show a helpful error
  echo "'$1' is not a known function name" >&2
  exit 1
fi

