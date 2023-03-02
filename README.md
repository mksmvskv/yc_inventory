# From this
```plain text
+----------------------+--------------+---------------+---------+----------------+-------------+
|          ID          |     NAME     |    ZONE ID    | STATUS  |  EXTERNAL IP   | INTERNAL IP |
+----------------------+--------------+---------------+---------+----------------+-------------+
| ffffffffffffffffffff | reddit-db    | ru-central1-a | RUNNING | 1.2.3.4        | 10.10.1.33 |
| ffffffffffffffffffff | jenkins      | ru-central1-a | STOPPED | 1.2.3.4        | 10.10.1.30 |
| ffffffffffffffffffff | webserver    | ru-central1-a | STOPPED | 1.2.3.4        | 10.10.1.13 |
| ffffffffffffffffffff | reddit-app   | ru-central1-a | RUNNING | 1.2.3.4        | 10.10.1.3  |
+----------------------+--------------+---------------+---------+----------------+-------------+

```
# Through this
```text
[reddit-db]
ansible_host=1.2.3.4
[jenkins]
ansible_host=1.2.3.4
[webserver]
ansible_host=1.2.3.4
[reddit-app]
ansible_host=1.2.3.4
```
# To this
```JSON
{
    "all": {
        "hosts": {
            "reddit-db": {
                "ansible_host": "1.2.3.4"
            },
            "jenkins": {
                "ansible_host": "1.2.3.4"
            },
            "webserver": {
                "ansible_host": "1.2.3.4"
            },
            "reddit-app": {
                "ansible_host": "1.2.3.4"
            }
        }
    }
}
```
