# 泛微OA 数据表: `info_journaltype`

- **中文名称**: 刊型信息表
- **所属模块**: `政务督办采编`
- **数据库表名**: `info_journaltype`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | 否 | 否 | - | - | 用于做主键返回 |
| 3 | `pathid` | 路径id | `integer` | - | 是 | 否 | 否 | - | - | info_path表主键id |
| 4 | `name` | 刊型名称 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 5 | `isused` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | 0否 1是 |
| 6 | `showorder` | 排序 | `float` | - | 是 | 否 | 否 | - | - | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 9 | `approve` | 是否审批 | `integer` | - | 是 | 否 | 否 | - | - | 0否 1是 |
| 10 | `doctemplate` | 文档模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `cycle` | 刊号周期 | `integer` | - | 是 | 否 | 否 | - | - | 0无 1月 2季 3年 |
| 12 | `maincategory` | 附件上传1级目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `subcategory` | 附件上传2级目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `seccategory` | 附件上传3级目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `additionalscore` | 特殊采用分值 | `float` | - | 是 | 否 | 否 | - | - | - |
| 16 | `specialscore` | 专报分值 | `float` | - | 是 | 否 | 否 | - | - | - |
