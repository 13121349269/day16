from django.db import models
from django.utils import timezone

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """人员"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    project_name = models.ForeignKey(verbose_name="关联项目", to="Project_list", to_field="id",on_delete = models.DO_NOTHING
                                     ,null=True)
    # password = models.CharField(verbose_name="密码", max_length=64, null=True)
    # age = models.IntegerField(verbose_name="年龄", null=True)
    # gender_choices = (
    #     (1, "男"),
    #     (2, "女")
    # )
    # gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, null=True)
    # #depart_id = models.SmallIntegerField(verbose_name="部门ID")
    # account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0, null=True)
    # create_time = models.DateField(verbose_name="入职时间", null=True)
    #约束
    # depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)

class Project_list(models.Model):
    """项目列表"""
    project_name = models.CharField(verbose_name="项目名称", max_length=64)
    change_time = models.DateField(verbose_name="修改时间",default=timezone.now)

    def __str__(self):
        return self.project_name


class Project_Msg(models.Model):
    """项目基础信息"""
    project = models.ForeignKey(verbose_name="项目名", to="Project_list", to_field="id", on_delete=models.CASCADE)
    group_coe = models.CharField(verbose_name="项目编码", max_length=64)
    namespace = models.CharField(verbose_name="命名空间", max_length=64)


class Project_Doc(models.Model):
    """项目文档"""
    project = models.ForeignKey(verbose_name="项目名", to="Project_list", to_field="id", on_delete=models.CASCADE)
    project_doc = models.FileField(verbose_name="项目文件", upload_to='project_doc')
    upload = models.FileField(upload_to='project_doc/')
    # upload_date = models.DateField(auto_now_add=True)
    # doc_time = models.DateTimeField(verbose_name="修改时间",auto_now_add=True)


class Link(models.Model):
    """访问链接"""
    # func = models.CharField(verbose_name="用途",null=True,max_length=12)
    name = models.CharField(verbose_name="链接名", max_length=64)
    link = models.CharField(verbose_name="链接", max_length=128)
    user_name = models.CharField(verbose_name="用户名", null=True, max_length=12)
    pwd = models.CharField(verbose_name="密码", null=True, max_length=32)
    other_1 = models.CharField(verbose_name="备注1", null=True, max_length=32)
    other_2 = models.CharField(verbose_name="备注2", null=True, max_length=32)


class Containerd(models.Model):
    """镜像"""
    name = models.CharField(verbose_name="服务名", max_length=32)
    port = models.CharField(verbose_name="端口", max_length=12, null=True)
    version = models.CharField(verbose_name="版本", max_length=12, null=True)
    url = models.CharField(verbose_name="镜像", max_length=256)
    date = models.DateField(verbose_name="更新时间", max_length=64)
    other_1 = models.CharField(verbose_name="备注1", null=True, max_length=32)
    other_2 = models.CharField(verbose_name="备注2", null=True, max_length=32)


class Middleware(models.Model):
    """中间件信息"""
    type = models.CharField(verbose_name="类型", max_length=12)
    name = models.CharField(verbose_name="服务名", max_length=12)
    func = models.CharField(verbose_name="功能", null=True, max_length=32)
    version = models.CharField(verbose_name="版本", null=True, max_length=12)
    hostname = models.CharField(verbose_name="主机名", null=True, max_length=64)
    public_network = models.CharField(verbose_name="公网链接方式", null=True, max_length=12)
    public_port = models.CharField(verbose_name="公网端口", null=True, max_length=12)
    intranet = models.CharField(verbose_name="内网链接方式", null=True, max_length=12)
    intranet_port = models.CharField(verbose_name="内网端口", null=True, max_length=12)
    username = models.CharField(verbose_name="用户名", null=True, max_length=12)
    passwd = models.CharField(verbose_name="密码", null=True, max_length=32)
    install_path = models.CharField(verbose_name="安装路径", null=True, max_length=128)
    data_paht = models.CharField(verbose_name="数据路径", null=True, max_length=128)
    start_command = models.CharField(verbose_name="启动命令", null=True, max_length=128)
    other_1 = models.CharField(verbose_name="备注1", null=True, max_length=32)
    other_2 = models.CharField(verbose_name="备注2", null=True, max_length=32)


class Servers(models.Model):
    """服务器信息"""
    type = models.CharField(verbose_name="类型", null=True, max_length=32)
    os = models.CharField(verbose_name="系统版本", null=True, max_length=32)
    hostname = models.CharField(verbose_name="实例名", null=True, max_length=32)
    func = models.CharField(verbose_name="用途", null=True, max_length=32)
    public_ip = models.CharField(verbose_name="外网IP", null=True, max_length=32)
    intranet_ip = models.CharField(verbose_name="内网ip", null=True, max_length=32)
    username = models.CharField(verbose_name="用户名", null=True, max_length=32)
    passwd = models.CharField(verbose_name="密码", null=True, max_length=32)
    sshport = models.CharField(verbose_name="ssh端口", null=True, max_length=12)
    CPU = models.CharField(verbose_name="cpu", null=True, max_length=12)
    memory = models.CharField(verbose_name="内存", null=True, max_length=12)
    server_disk = models.CharField(verbose_name="系统盘", null=True, max_length=12)
    data_disk = models.CharField(verbose_name="数据盘", null=True, max_length=12)
    disk_type = models.CharField(verbose_name="磁盘类型", null=True, max_length=12)
    host_type = models.CharField(verbose_name="机器类型", null=True, max_length=12)
    other_1 = models.CharField(verbose_name="备注1", null=True, max_length=32)
    other_2 = models.CharField(verbose_name="备注2", null=True, max_length=32)
