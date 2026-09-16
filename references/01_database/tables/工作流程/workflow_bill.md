# 泛微OA 数据表: `workflow_bill`

- **中文名称**: 工作流单据信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_bill`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `clazz` | 系统单据继承类 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `namelabel` | 单据显示名称 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `tablename` | 对应的主表名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 5 | `createpage` | 创建请求页面url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `managepage` | 管理请求页面url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `viewpage` | 查看请求页面url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `detailtablename` | 对应的从表名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 9 | `detailkeyfield` | 从表链接主表的关键字 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 10 | `operationpage` | 后台处理请求页面url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `hasfileup` | 已有文件上传 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `invalid` | 无效标志 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `formdes` | 表单描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `subcompanyid` | 子公司id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `dsporder` | 显示顺序 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 16 | `subcompanyid3` | 子公司id3 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `from_module_` | 表单模块 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
