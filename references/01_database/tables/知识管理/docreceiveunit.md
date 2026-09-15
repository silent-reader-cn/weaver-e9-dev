# 泛微OA 数据表: `docreceiveunit`

- **所属模块**: `知识管理`
- **数据库表名**: `docreceiveunit`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `unitcode` | 编码 | `varchar2` | 800 | 是 | - |
| 2 | `id` | 收文单位id | `integer` | - | 否 | - |
| 3 | `receiveunitname` | 收文单位名称 | `varchar2` | 1000 | 是 | - |
| 4 | `superiorunitid` | 上级单位id | `integer` | - | 是 | - |
| 5 | `receiverids` | 收文员 | `varchar2` | 4000 | 是 | - |
| 6 | `allsuperiorunitid` | 所有上级单位id | `varchar2` | 640 | 是 | 以,号分开 |
| 7 | `unitlevel` | 单位级别 | `integer` | - | 是 | - |
| 8 | `canceled` | 是否封存 | `char` | 1 | 是 | 1：是，0或其它：否 |
| 9 | `companytype` | 单位类型 | `varchar2` | 8 | 是 | - |
| 10 | `ismain` | 是否主送方 | `varchar2` | 8 | 是 | - |
| 11 | `changedir` | 公文交换目录 | `varchar2` | 800 | 是 | - |
| 12 | `subcompanyid` | 分部 | `integer` | - | 是 | - |
| 13 | `canstartchildrequest` | 是否可启动收文流程 | `char` | 1 | 是 | - |
| 14 | `showorder` | 顺序 | `number` | (15,2) | 是 | - |
