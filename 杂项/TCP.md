# 1、三次握手
## 标志位
- SYN 发起一个连接
- ACK 应答确认
- FIN 释放连接

三次握手的目的是连接服务器指定端口，建立TCP连接，并同步连接双方的序列号和确认号，交换TCP窗口大小信息。在socket编程中，客户端执行connect()时将触发三次握手。

- 第一次握手 客户端发送SYN=1 seq=xz(客户端SYN_send)
- 第二次握手 服务端发送ACK=1 SYN=1 ack=x+1 seq=y(服务端SYN_RESV)
- 第三次握手 客户端发送ACK=1 ack=y+1 seq=x+1 SYN=0(客户端发送后ESTABLISHED,服务端收到ESTABLISHED)

