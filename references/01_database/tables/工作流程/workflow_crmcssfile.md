# 泛微OA 数据表: `workflow_crmcssfile`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_crmcssfile`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `cssname` | css文件显示名 | `varchar2` | 1000 | 是 | - |
| 3 | `realfilename` | css文件在服务器上的名字 | `varchar2` | 1000 | 是 | - |
| 4 | `realpath` | css在服务器上的存储全路径 | `varchar2` | 2000 | 是 | - |
| 5 | `type` | 类型 | `integer` | - | 是 | - |
