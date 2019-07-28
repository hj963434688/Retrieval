图像检索：
    本项目为图像检索后端服务 用于搜索相似图像 主要服务对象为：面料（material）配件（parts）鞋款（shoes）

环境搭建：
  
    cuda 和 cudnn 选择与显卡对应版本的进行下载安装 具体可以查询网上教程
    Python3 使用anaconda3库 下载对应系统版本安装 记得添加到环境变量
    tensorflow 控制台使用 pip install tensorflow-gpu 安装
    其他缺失的库可以通过conda 或 pip 命令安装


文件说明：

    --config: 全局配置文件
    --database: 数据库存放位置 目前所以的数据是以txt文件储存 
        单行存储信息格式为图片url+图像编码结果（二进制）+label(颜色 图片ID等)后续可以加入其他备注信息
    --json_file: 图片分类辅助文件 存放图片分类信息 目前暂时没有用到 后续如果要自行训练可能要用到
    --nets:存放标准网络文件
        --vgg.py vgg网络
    --pre-trained-models:预训练模型存放 由于模型较大 现在将它放在上一层目录中
    --util:一些辅助函数工具包
    --init.py: 用于后台批量从原始图片初始化数据库
    --net.py.py: 网络配置文件（暂未使用）
    --network.py： 网络服务类的定义 和关键的内部操作
    --nnflask.py: web接口 提供查询插入删除等接口 也是后台运行的入口
    --operate.py: 主要的查询插入删除函数实现
    --clear.py : 清除指定txt文件
    详情看代码注释

运行说明：
    
    在当前目录下 运行 python nnflask.py 等待程序加载完毕在浏览器输入链接即可返回结果

链接格式：
    
    参数： URL 图片链接  num 返回结果数量
        tag 搜索类型 0 面料  1 配件 
    检索图片：
        格式： http://ip:9999/image?url=url&num=num&tag=0 
        返回: 404 输入图片链接无效 500 获取url出错 555 服务器运行出错

    添加图片
        格式 http://127.0.0.1:9999/image/add?url=url&tag=0
        返回：404 输入图片链接无效 500 获取url出错 111 该图片链接已经在数据库中
          555 服务器运行出错

    删除图片
        格式 http://127.0.0.1:9999/image/delete?url=url&tag=0
        返回：222 该图片不存在 500 获取url出错 555 服务器运行出错
作者：何海君 华南农业大学 
 
