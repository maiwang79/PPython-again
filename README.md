# PPython

PPython 是 PHP 结合 Python 的开发技术，最初见于 [https://code.google.com/p/ppython](https://code.google.com/p/ppython)，系由 [LAJP](https://code.google.com/p/lajp)演变而来。LAJP 是 PHP 结合 JAVA 的开发技术，提供 PHP 结合 JAVA 的融合能力。PPython 将此种融合能力移到 Python 上，其在 Python 端启动进程监听访问，PHP 端可使用封装后的函数向 Python 端发起请求，执行任意 Python 模块的函数调用，运行结果以序列化数据返回给 PHP 进程，使 PHP 与 Python 实现无碍通讯。

PPython 项目似已停止维护，作者是 diaoyifei。在 Google Code 停止运营之后，在 GitHub 上未找到该库的新仓库地址，特此将此仓库重新部署到 GitHub 上，并遵循其 Apache 许可证进行进一步开发和维护。

# 安装

安装之前先要已有可正常工作的 PHP 及 PYTHON 3 运行环境，PHP 端及 Python 端可以位于不同主机，保持通讯正常即可。

将本仓库下载后的文件解压于一个目录，可以是任意目录，记为 `{PPYTHON_PATH}`。

根据需要，其它文件可以分开部署，`php_python.py` 与 `process.py` 须在 `{PPYTHON_PATH}` 下。

在 `php_python.py` 中设定 `LISTEN_PORT`，并在 `php_python.php` 中修改 `LAJP_IP` 和 `LAJP_PORT` 值，使两处保持一致。

如准备将 PPython 配置为服务，将 `ppython.service` 复制到 `/usr/lib/systemd/system/` 下，并将其中的 `{PPYTHON_PATH}` 改为实际路径。运行以下命令可使 `ppython` 服务在系统启动时自动运行：

```
chkconfig ppython on
```

# 用法

命令行运行 `php_python.py`，或启动 `ppython` 服务，确认 Python 已按设定端口进行监听。

在 PHP 项目中引入 `{PPYTHON_PATH}/php/php_python.php`，在需要执行 Python 处理的位置添加以下代码：

```
$result = ppython({python_func},{params}...)
```

其中 `{python_func}` 是希望调用的 Python 函数，如 `test::go`，相应地 `{PPYTHON_PATH}` 下应具有 `test.py` 文件，且其中存在 `go` 函数。运行结果保存在 `$result` 中，可以是数组或对象等复杂结构。`{params}` 可以是 0 个或任意多个，按普通 PHP 调用方式传递即可。

传递参数与返回结果数据结构不限，只需 PHP 与 Python 端均能识别其序列化与反序列化，PHP 端由 `serialize()` 与 `unserialize()` 处理，Python 端由 `process.py` 中的 `z_encode()` 与`z_decode()` 函数支持完成转换。

# 欢迎反馈和参考贡献

这种将 Python 和 PHP 连接起来的方式不同于简单的 `exec()`、`system()` 方式，具有一定的创新性和优势，欢迎对此方式感兴趣的同学贡献代码和反馈。
