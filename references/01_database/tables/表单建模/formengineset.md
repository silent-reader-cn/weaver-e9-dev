# 泛微OA 数据表: `formengineset`

- **所属模块**: `表单建模`
- **数据库表名**: `formengineset`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `waterimg` | 水印图片 | `varchar2` | 100 | 是 | - |
| 2 | `wateralpha` | 水印透明度 | `varchar2` | 10 | 是 | - |
| 3 | `id` | 主键id | `integer` | - | 否 | - |
| 4 | `appid` | 应用id | `integer` | - | 是 | 对应应用信息表中id |
| 5 | `modeid` | 模块id | `integer` | - | 是 | 对应模块信息表中id |
| 6 | `initformmodereply` | 是否初始化表单建模回复 | `integer` | - | 是 | 0--否，1--是 |
| 7 | `isenformmodereply` | 是否开启表单建模回复 | `integer` | - | 是 | 0--否，1--是 |
| 8 | `isdelete` | 是否删除 | `integer` | - | 是 | 0--否，1--是 |
| 9 | `watertype` | 水印属性 | `varchar2` | 1 | 是 | - |
| 10 | `waterfont` | 水印文字 | `varchar2` | 100 | 是 | - |
| 11 | `watercolor` | 水印颜色 | `varchar2` | 100 | 是 | - |
| 12 | `watersize` | 水印大小 | `integer` | - | 是 | - |
| 13 | `watercontent` | 水印内容 | `varchar2` | 4000 | 是 | - |
| 14 | `type` | 标准、无边距、自定义边距 | `varchar2` | 2000 | 是 | - |
| 15 | `topty` | 上 | `integer` | - | 是 | - |
| 16 | `leftey` | 左 | `integer` | - | 是 | - |
| 17 | `bottom` | 下 | `integer` | - | 是 | - |
| 18 | `rightey` | 右 | `integer` | - | 是 | - |
