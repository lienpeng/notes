- SPI 
service provider interface
需要在resources目录下新建META-INF/services目录(建目录的时候一层一层建，不然可能出现META-INF.services的路径，导致拿不到实现类)，并且在这个目录下新建一个与接口S的全限定名(package)一致的文件，在这个文件中写入接口的实现类impl的全限定名
通过serviceLoader加载实现类并调用
`ServiceLoader<S> uploadCDN = ServiceLoader.load(S.class)`

Java SPI 就是把某个接口的 指定实现类 （通过在指定文件配置的方式）给实例化出来了。

需要让上层知道该调用哪个具体实现


<T> 泛型，可以传入具体的参数类型
<?> 类型通配符 代表任意类型实参

Class.forName( )静态方法的目的是为了动态加载类
在JVM加载指定类的过程中，如果类中有静态初始化内容的话，JVM就会执行该部分代码
JDBC规范要求任何一个driver类必须向DriverManger类去注册自己

**了解classload加载机制 双亲委托**

*实现一个listener*


- laf-extension
封装了ServiceLoader，默认使用ServiceLoader，也可以使用spring加载器
使用方式：
在resources目录下新建META-INF/services目录；
在项目更目录建立Plugin.java 定义拓展常量
ExtensionPoint<JsonProvider, String> JSON = new ExtensionPointLazy(JsonProvider.class);
JsonProvider 为拓展使用的接口 ；ExtensionPointLazy实现了延迟加载，在后续实例化具体的接口实现类
调用的时候 JSON.get(String)该方法实现会初始化实现类

- laf-binding




