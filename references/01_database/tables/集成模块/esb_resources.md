# 泛微OA 数据表: `esb_resources`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_resources`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `resid` | 资源标识 | `varchar2` | 100 | 否 | - |
| 2 | `resname` | 资源名称 | `varchar2` | 1000 | 是 | - |
| 3 | `restype` | 资源类型 | `varchar2` | 80 | 是 | - |
| 4 | `resstatus` | 资源状态 | `char` | 1 | 是 | 1:启用，0未启用 |
| 5 | `params` | 参数信息 | `clob` | 4000 | 是 | - |
| 6 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 7 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | - |
| 8 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | - |
| 9 | `modifytime` | 修改时间 | `varchar2` | 80 | 是 | - |
