tc qdisc add dev eth0 root handle 1: prio
tc filter add dev eth0 parent 1:0 protocol ip prio 1 u32 match ip dst 10.179.20.0/24 flowid 2:1
tc qdisc add dev eth0 parent 1:1 handle 2: netem delay 10ms

tc qdisc add dev eth0 root handle 1: prio
tc filter add dev eth0 parent 1:0 protocol ip prio 1 u32 match ip dst 172.28.228.78 flowid 2:1
tc filter add dev eth0 parent 1:0 protocol ip prio 1 u32 match ip dst 172.28.228.77 flowid 2:1
tc qdisc add dev eth0 parent 1:1 handle 2: netem delay 100ms


tc qdisc del dev eth0 root


tc qdisc [ add | change | replace | link ] dev DEV [ parent qdisc-id | root ] [ handle qdisc-id ] qdisc [ qdisc specific parameters ]

tc class [ add | change | replace ] dev DEV parent qdisc-id [ classid class-id ] qdisc [ qdisc specific parameters ]

tc filter [ add | change | replace ] dev DEV [ parent qdisc-id | root ] protocol protocol prio priority filtertype [ filtertype specific parameters ] flowid flow-id

tc [-s | -d ] qdisc show [ dev DEV ]

tc [-s | -d ] class show dev DEV tc filter show dev DEV

队列规定 qdisc(queueing discipline )、类(class)和分类器(Classifiers)
tc class上的parent :参数是队列ID。classid是自己的ID。
tc qdisc parent 参数是类的ID。

所有的QDisc、类和过滤器都有ID。ID可以手工设置，也可以有内核自动分配。ID由一个主序列号和一个从序列号组成，两个数字用一个冒号分开。一个QDisc会被分配一个主序列号，叫做句柄(handle)，然后把从序列号作为类的命名空间。句柄采用10:一样的表达方式。习惯上，需要为有子类的QDisc显式地分配一个句柄。同一个QDisc里面的类分享这个QDisc的主序列号，但是每个类都有自己的从序列号，叫做类识别符(classid)。类识别符只与父QDisc有关，和父类无关。类的命名习惯和QDisc的相同。

一般情况下，针对一个队列需建立一个根分类，然后再在其上建立子分类。对于分类，按其分类的编号顺序起作用，编号小的优先；一旦符合某个分类匹配规则，通过该分类发送数据包，则其后的分类不再起作用。

复杂的队列（Qdisc）需要使用不同的过滤器(Filter)来把报文分组分成不同的类别(Class)。这里把这些复杂的队列称为可分类(Classiful)的队列


jmq2发送超时2秒
tc qdisc show    # 显示
tc qdisc  add dev eth0 root ...... # 加入
tc qdisc  change  dev eth0 root ...... # 修改存在的 qdisc ,记的,加入同一条后只能用 change 来修改
tc qdisc del dev eth0 root  # 删除

延迟
tc qdisc add dev eth0 root netem delay 3000ms
丢包
tc qdisc change dev eth0 root netem loss 50%

定义顶层/根队列规则，指定default类别编号
tc qdisc add dev eth0 root handle 1: htb default 2
定义第一层的 1:1 类别 
tc class add dev eth0 parent 1:1 classid 1:2 htb rate 98mbit ceil100mbit prio 2 
tc class add dev eth0 parent 1:1 classid 1:3 htb rate 1mbit ceil 2mbit prio 2

tc filter add dev eth0 protocol ip parent 1:0 u32 match ip src 192.168.0.2 flowid 1:2



tc qdisc add dev eth0 root handle 1: prio

tc qdisc add dev eth0 root handle 1: netem loss 50%
tc class add dev eth0 parent 1: classid 1:1 htb rate 100Mbps
tc filter add dev eth0 parent 1: protocol ip prio 1 u32 match ip dst 172.28.159.13 flowid 1:1




# 这个命令立即创建了类: 1:1, 1:2, 1:3  队列缺省1:0
tc qdisc add dev eth0 root handle 1: prio
一般情况下，针对一个队列需建立一个根分类，然后再在其上建立子分类。对于分类，按其分类的编号顺序起作用，编号小的优先；一旦符合某个分类匹配规则，通过该分类发送数据包，则其后的分类不再起作用。
过滤器主要服务于分类。
一般只需针对根分类提供一个过滤器，然后为每个子分类提供路由映射。
在1:节点添加一个过滤规则,优先权1:凡是去往的IP数据包,发送到频道2:1
tc filter add dev eth0 parent 1:0 protocol ip prio 1 u32 match ip dst 172.28.159.13 flowid 2:1
tc qdisc add dev eth0 parent 1:1 handle 2: netem delay 100ms
# 此命令立即创建了类 : 2:1, 2:2, 2:3 ( 缺省三个子类 ) ) 

根据源/目的地址
源地址段：match ip src 1.2.3.0/24
目的地址段：match ip dst 4.3.2.0/24
单个IP地址：match ip 1.2.3.4/32

根据源/目的端口,所有IP协议
源端口80：match ip sport 80 0xffff，其中0xffff表示所有数据包
目的端口80：match ip dport 80 0xffff
根据IP协议 (tcp, udp, icmp, gre, ipsec)
icmp是1:match ip protocol 1 0xff，其中 1是根据/etc/protocols协议号来设定
根据fwmark

#iptables -A PREROUTING -t mangle -i eth0 -j MARK --set-mark 6
#tc filter add dev eth1 protocol ip parent 1:0 prio 1 handle 6 fw flowid 1:1


tc qdisc add dev eth0 root handle 1: prio
tc filter add dev eth0 parent 1:0 protocol ip prio 1 u32 match ip dst 11.53.232.144/32 flowid 2:1
tc qdisc add dev eth0 parent 1:1 handle 2: netem delay 2100ms

tc qdisc del dev eth0 root
