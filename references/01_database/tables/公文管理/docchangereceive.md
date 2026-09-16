# 泛微OA 数据表: `docchangereceive`

- **中文名称**: 公文交换接收信息表
- **所属模块**: `公文管理`
- **数据库表名**: `docchangereceive`
- **主键**: `id`
- **字段数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `type` | 类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 3 | `imagefileid` | 文档编号 | `integer` | - | 是 | 是 | 否 | - | - | 对应imagefile表中的编号 |
| 4 | `sn` | 文号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `title` | 标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `companyid` | 单位编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `version` | 版本 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `senddate` | 发送日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 9 | `sendtime` | 发送时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 10 | `receivedate` | 接收日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 11 | `receivetime` | 接收时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 12 | `executedate` | 处理日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 13 | `executetime` | 处理时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 14 | `receiver` | 接收者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `docid` | 正文编号 | `integer` | - | 是 | 是 | 否 | - | - | 对应docimagefile表中的docid |
| 16 | `fileids` | 字段编号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `iscreatewf` | 是否创建流程 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 18 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `chageflag` | 是否交换 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 20 | `flagtitle` | 标记标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
