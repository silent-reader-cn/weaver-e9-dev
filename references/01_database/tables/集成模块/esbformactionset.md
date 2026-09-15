# 泛微OA 数据表: `esbformactionset`

- **所属模块**: `集成模块`
- **数据库表名**: `esbformactionset`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 主键 |
| 2 | `actionname` | 接口名称 | `varchar2` | 1000 | 是 | ESB接口名称 |
| 3 | `showname` | 显示名 | `varchar2` | 1000 | 是 | 显示名 |
| 4 | `formid` | 流程表单ID | `integer` | - | 是 | 流程表单ID |
| 5 | `isbill` | 是否单据 | `integer` | - | 是 | 是否单据 |
| 6 | `esbid` | ESB主键 | `varchar2` | 800 | 是 | ESB所发布服务的主键 |
| 7 | `esbname` | ESB名称 | `varchar2` | 800 | 是 | ESB发布服务的名称 |
| 8 | `version` | ESB版本 | `integer` | - | 是 | ESB所发布的服务的版本，当版本低于生效版本时提示当前设置已失效 |
| 9 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 10 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |
| 11 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 12 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 修改时间 |
| 13 | `returnrulerelationship` | 返回规则关系 | `char` | 1 | 是 | 返回规则关系，多个返回值之间的关系为与关系还是或关系 |
