Run a simple daemon listening to ntfy notifications using supervisord.

 1. Run a ntfy server:  `ntfy serve --listen-http :9999`
 2. Run the listener daemon with supervisord: `supervisord -n`
 3. Tail the dameon stdout: `supervisorctl tail -f listener`
 4. Publish to the topic: `curl -d '{"ham": "cheese", "spam":{"eggs": 3}}' localhost:9999/my-topic`.



