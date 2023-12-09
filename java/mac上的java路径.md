java命令的完整路径是/usr/bin/java，这个java是软连接，它其实了/System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands/java，由于Current也是一个软连接，其实是/System/Library/Frameworks/JavaVM.framework/Versions/A/Commands/java。A/Commands中的java我理解，它其实是从别的地方拷贝过来的。如果我们没有设置java的环境变量，默认的java是/usr/libexec/java_home命令指出的java，在我的电脑上是/Library/Java/JavaVirtualMachines/jdk-11.0.2.jdk/Contents/Home/bin/java，如果我们有设置java环境变量，那么就是我们配置的java了，在我的电脑上是/Applications/Android\ Studio.app/Contents/jre/jdk/Contents/Home/bin/java


查看软链接 ls -l
