# 泛微OA 数据表: `formmodelog`

- **中文名称**: 后台操作日志表
- **所属模块**: `表单建模`
- **数据库表名**: `formmodelog`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 操作时间，显示形式2 8 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `objid` | 操作对象 | `varchar2` | 50 | 是 | 否 | 否 | - | - | 结合操作模块使用 |
| 3 | `logmodule` | 操作模块 | `varchar2` | 20 | 是 | 否 | 否 | - | - | app:应用<br>form:表单<br>model:模块<br>search:查询<br>report:报表<br>browser:浏览框<br>tree:树<br>page:自定义<br>select:选择项<br>remindjob:提醒 |
| 4 | `logtype` | 操作类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | add：新建<br>edit：编辑<br>delete：删除 |
| 5 | `operator` | 操作者 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 操作者id，对应hrmresource表的id，1表示系统管理员 |
| 6 | `operatorname` | 操作者姓名 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 对应操作者的姓名 |
| 7 | `optdatetime` | 操作时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 操作时间，显示形式1 |
| 8 | `optdatetime2` | 操作时间2 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 操作时间，显示形式2 |
