# 泛微OA 数据表: `info_journal`

- **所属模块**: `政务应用`
- **数据库表名**: `info_journal`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 所属路径 | `integer` | - | 是 | 0期刊1专报2特殊采用 |
| 4 | `type` | 期刊类型 | `integer` | - | 是 | - |
| 5 | `title` | 发文标题 | `varchar2` | 256 | 是 | - |
| 6 | `creater` | 创建人 | `integer` | - | 是 | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | - |
| 9 | `j_type` | 所属刊型 | `integer` | - | 是 | - |
| 10 | `periods` | 期数 | `integer` | - | 是 | - |
| 11 | `docid` | 公文id | `integer` | - | 是 | - |
| 12 | `status` | 状态 | `integer` | - | 是 | 0未成文,1已成文,2未发布,3审批中,4驳回,5已发布 |
| 13 | `cycle` | 当前数据的周期格式 | `varchar2` | 10 | 是 | 0无 XXXX-XX月 XXXX,X季度 XXXX年 |
| 14 | `discard` | 是否废弃 | `integer` | - | 是 | 0否 1是 |
| 15 | `atach` | 附件 | `clob` | - | 是 | - |
| 16 | `editer` | 编辑人 | `integer` | - | 是 | - |
| 17 | `editdate` | 编辑日期 | `varchar2` | 10 | 是 | - |
| 18 | `edittime` | 编辑时间 | `varchar2` | 8 | 是 | - |
| 19 | `finalizer` | 定稿人 | `integer` | - | 是 | - |
| 20 | `finalizedate` | 定稿日期 | `varchar2` | 10 | 是 | - |
| 21 | `finalizetime` | 定稿时间 | `varchar2` | 8 | 是 | - |
| 22 | `releaser` | 发布人 | `integer` | - | 是 | - |
| 23 | `releasedate` | 发布日期 | `varchar2` | 10 | 是 | - |
| 24 | `releasetime` | 发布时间 | `varchar2` | 8 | 是 | - |
