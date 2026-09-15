# 泛微OA 数据表: `info_journaltype`

- **所属模块**: `政务应用`
- **数据库表名**: `info_journaltype`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | 用于做主键返回 |
| 3 | `pathid` | 路径id | `integer` | - | 是 | info_path表主键id |
| 4 | `name` | 刊型名称 | `varchar2` | 256 | 是 | - |
| 5 | `isused` | 是否启用 | `integer` | - | 是 | 0否 1是 |
| 6 | `showorder` | 排序 | `float` | - | 是 | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | - |
| 9 | `approve` | 是否审批 | `integer` | - | 是 | 0否 1是 |
| 10 | `doctemplate` | 文档模板id | `integer` | - | 是 | - |
| 11 | `cycle` | 刊号周期 | `integer` | - | 是 | 0无 1月 2季 3年 |
| 12 | `maincategory` | 附件上传1级目录 | `integer` | - | 是 | - |
| 13 | `subcategory` | 附件上传2级目录 | `integer` | - | 是 | - |
| 14 | `seccategory` | 附件上传3级目录 | `integer` | - | 是 | - |
| 15 | `additionalscore` | 特殊采用分值 | `float` | - | 是 | - |
| 16 | `specialscore` | 专报分值 | `float` | - | 是 | - |
