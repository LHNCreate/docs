### COMMONAPI SOMEIP DEMO

可作为CommonAPI SomeIP的使用示例

#### Dependencies

安装依赖：

```bash
sudo apt-get install cmake cmake-qt-gui libexpat-dev expat default-jre
```

编译和安装 boost：

```bash
cd boost_1_57_0
./bootstrap.sh
./b2 link=shared
sudo ./b2 install
```

编译和安装 vsomeip：

```bash
git clone https://github.com/GENIVI/vsomeip.git
cd vsomeip
mkdir build
cd build
cmake -DENABLE_SIGNAL_HANDLING=1 -DDIAGNOSIS_ADDRESS=0x10 ..
make
sudo make install
```

编译和安装 CommonAPI Core Runtime：

```bash
git clone https://github.com/GENIVI/capicxx-core-runtime.git
cd capicxx-core-runtime/
mkdir build
cd build
cmake ..
make
sudo make install
```

编译和安装 CommonAPI SomeIP Runtime：

```bash
git clone https://github.com/GENIVI/capicxx-someip-runtime.git
cd capicxx-someip-runtime/
mkdir build
cd build
cmake -DUSE_INSTALLED_COMMONAPI=OFF ..
make
sudo make install
```

切换JAVA版本到Oracle jdk1.8：

```bash
sudo update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_281/bin/java 700
sudo update-alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_281/bin/javac 700
sudo update-alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_281/bin/jar 700
sudo update-alternatives --config java # 选择jdk1.8
java -version # 检查是否配置成功
```

CommonAPI Core Runtime代码生成工具：

> `CommonAPI/commonapi_core_generator_2/commonapi-core-generator-linux-x86_64`

CommonAPI SomeIP Runtime代码生成工具：

> `CommonAPI/commonapi_someip_generator/commonapi-someip-generator-linux-x86_64`



#### demo创建

创建工程目录：

```bash
mkdir helloworld
```

创建fidl目录

`mkdir fidl`

`cd fidl`

创建helloworld.fidl:

`touch helloworld.fidl`

内容如下：

```
package commonapi
interface helloworld {
  version {major 1 minor 0}
  method sayHello {
    in {
      String name
    }
    out {
      String message
    }
  }
}
```

创建helloworld.fdepl

`touch helloworld.fdepl`

内容如下：

```
import "platform:/plugin/org.genivi.commonapi.someip/deployment/CommonAPI-SOMEIP_deployment_spec.fdepl"
import "helloworld.fidl"

define org.genivi.commonapi.someip.deployment for interface commonapi.helloworld {
  SomeIpServiceID = 4660
  method sayHello {
    SomeIpMethodID = 123
  }
}

define org.genivi.commonapi.someip.deployment for provider as MyService {
  instance commonapi.helloworld {
    InstanceId = "test"
    SomeIpInstanceID = 22136
  }
}
```



生成代码：

```bash
./../commonapi_core_generator/commonapi-core-generator-linux-x86_64 -sk ./fidl/helloworld.fidl
./../commonapi_someip_generator/commonapi-someip-generator-linux-x86_64 ./fidl/helloworld.fdepl
```

这个操作会在项目文件夹下生成一个`src-gen`文件夹

`然后添加你的实现代码`

> 注：./为当前目录，../为上一级目录 具体文件位置请视自己的情况而定

编译工程：

```bash
mkdir build
cd build
cmake ..
make
```