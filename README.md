# Apache Spark


# Instalação e configuração do spark para ambiente local Windows e WSL Ubuntu 20.04


## Instalando Spark
* Baixe apache spark consulte versão mais recente [Download](https://spark.apache.org/downloads.html).
  * `wget https://www.apache.org/dyn/closer.lua/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz`
* Criar o diretório do spark `sudo mkdir -p /usr/local/spark`
* Descompactar arquivo no diretório spark criado anteriormente `tar -xvzf spark-3.3.0-bin-hadoop3.tgz -C /usr/local/spark`.
* Remova o arquivo que foi baixado do spark `rm -r spark-3.3.0-bin-hadoop3.tgz`.

## Configurando Python e Pyspark
* Instale o java na sua maquina `sudo apt install openjdk-17-jdk -y`
* Verifique a versão do python necessária >= 3.7 para a versão instalada acima `python -V`
* Instale o [PYENV](https://github.com/pyenv/pyenv-installer) para gerenciamento do ambiente virtual do Python.
* Crie um ambiente virtual `pyenv virtualenv <versão do python> <nome_do_virtual_env>` no meu caso realizei `pyenv virtualenv 3.8.10 spark`.
* Adicione as seguintes variáveis no seu bash no arquivo exemplo `sudo vim ~/.bashrc`.
    ```
    # Configurações do Poderoso SPARK
    export SPARK_HOME="/usr/local/spark/spark-3.3.0-bin-hadoop3"
    export PATH="${PATH}:${SPARK_HOME}/bin"

    # Configurações Pyspark
    export PYSPARK_PYTHON="$HOME/.pyenv/versions/spark/bin/python"
    export PYSPARK_DRIVER_PYTHON="$HOME/.pyenv/versions/spark/bin/python"

    # POWER MEGA JAVA_HOME
    export JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
    ```
* Reinicie o seu shell `source ~/.bashrc`, se ocorrer tudo certo esse comando não deve ter nenhum retorno no terminal.
* Validando instalação spark e pyspark `$SPARK_HOME/bin/./pyspark` o retorno precisa ser algo semelhante ao que esta abaixo.
    ```
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    22/09/01 14:49:02 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.3.0
      /_/

    Using Python version 3.8.9 (default, Aug 31 2022 23:17:58)
    Spark context Web UI available at http://172.29.92.99:4040
    Spark context available as 'sc' (master = local[*], app id = local-1662054543325).
    SparkSession available as 'spark'.
    >>>
    ```
  * Testando script `(spark)  heliezer@dev  ~/study/spark  python $PWD/spark_session.py`
      ```
      (spark)  heliezer@dev  ~/study/spark  python $PWD/spark_session.py
      22/09/01 16:32:59 WARN Utils: Your hostname, dev resolves to a loopback address: 127.0.1.1; using 172.29.92.99 instead (on interface eth0)
      22/09/01 16:32:59 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
      Setting default log level to "WARN".
      To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
        22/09/01 16:33:00 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
        +---------+----------+--------+----------+------+------+
        |firstname|middlename|lastname|       dob|gender|salary|
        +---------+----------+--------+----------+------+------+
        |    James|          |   Smith|1991-04-01|     M|  3000|
        |  Michael|      Rose|        |2000-05-19|     M|  4000|
        |   Robert|          |Williams|1978-09-05|     M|  4000|
        |    Maria|      Anne|   Jones|1967-12-01|     F|  4000|
        |      Jen|      Mary|   Brown|1980-02-17|     F|    -1|
        +---------+----------+--------+----------+------+------+
      ```