if [ $# -lt 1 ]; then
        echo 'give 1 argument'
else
        if [ $1 = 'list' ]; then
                curl -H "Content-type: application/json" -X POST -d '{"top_k":"10"}' http://203.255.81.132:10101/api-list >> ret
        fi
fi
