# 泛微OA 数据表: `mode_custompagedetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_custompagedetail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `mainid` | 自定义页面主id | `integer` | - | 否 | 对应mode_custompage表的id |
| 3 | `hrefname` | 名称 | `varchar2` | 1000 | 是 | 自定义页面名称 |
| 4 | `hreftitle` | 提示信息 | `varchar2` | 1000 | 是 | - |
| 5 | `hrefdesc` | 描述 | `varchar2` | 1000 | 是 | - |
| 6 | `hrefaddress` | 链接地址 | `varchar2` | 2000 | 是 | 自定义页面地址 |
| 7 | `disorder` | 显示顺序 | `number` | (15,2) | 是 | 显示顺序 |
