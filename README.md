# test-logs

> Se pueden plantear distintas soluciones:
1. Batch, con ventana de una hora
2. Streaming, analizando cada registro nuevo entrante

> He optado por la solución de Streaming, pero analizaremos brevemente una posible solución en Batch:

> Por ejemplo, suponemos que los ficheros de logs se escriben en HDFS o S3, y donde lo particionaríamos tal que la estrucutura de directrorios fuese:
logs/<aaaaammddhh>/, por lo que solo tendríamos que ejecutar cada hora un script, por ejemplo en .hql de HIVE, sobre dicho directorio, y creando previamente una EXTERNAL TABLE donde se mapearían los tres campos.

> Las queries serían de tipo:
```
1. SELECT host_client FROM <PARAMETER_0> WHERE hosts_servers = <PARAMETER_1>
2. SELECT host_server FROM <PARAMETER_0> WHERE hosts_clients = <PARAMETER_2>
3. SELECT host_client, COUNT(*) as cnt FROM <PARAMETER_0> GROUP BY host_client ORDER BY cnt DESC LIMIT 1; 
```
> Donde <PARAMETER_0>: Directorio fuente: logs/<aaaaammddhh>
        <PARAMETER_1>: El hostname donde se conectan (server) y por el que buscar clientes
        <PARAMETER_2>: El hostname que se conecta (client) y por el que buscar servidores

> Pasamos a analizar la solución de Streaming realizada en Python, donde podemos ver el código [aquí](https://github.com/rpmaya/test-logs/blob/master/src/logs.py):

> El script requiere de tres parámetros:
1. Fichero de entrada
2. Hostname del cliente por el que realizar la consulta
3. Hostname del server por el que realizar la consulta

> Por lo tanto ejecutaríamos tal que:
```
# python logs.py <LOG_PATH> <HOST_CLI> <HOST_SRV>
```





