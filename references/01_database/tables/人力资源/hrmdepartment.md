# 泛微OA 数据表: `hrmdepartment`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmdepartment`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `modified` | 修改时间 | `timestamp(6)` | 11 | 是 | 修改时间 |
| 2 | `modifier` | 修改人 | `integer` | - | 是 | 修改人 |
| 3 | `id` | ID | `integer` | - | 否 | ID |
| 4 | `departmentmark` | 部门标识 | `varchar2` | 480 | 是 | 部门标识 |
| 5 | `departmentname` | 部门名称 | `varchar2` | 1000 | 是 | 部门名称 |
| 6 | `subcompanyid1` | 所属分部1 | `integer` | - | 是 | 所属分部1 |
| 7 | `supdepid` | 上级部门id | `integer` | - | 是 | 上级部门id |
| 8 | `allsupdepid` | 所有上级部门id | `varchar2` | 2000 | 是 | 所有上级部门id |
| 9 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |
| 10 | `canceled` | 封存标识 | `char` | 1 | 是 | 封存标识 |
| 11 | `departmentcode` | 部门编码 | `varchar2` | 800 | 是 | 部门编码 |
| 12 | `coadjutant` | 协办人 | `integer` | - | 是 | 协办人 |
| 13 | `zzjgbmfzr` | 组织架构部门负责人 | `varchar2` | 4000 | 是 | 组织架构部门负责人 |
| 14 | `zzjgbmfgld` | 组织架构部门分管领导 | `varchar2` | 4000 | 是 | 组织架构部门分管领导 |
| 15 | `jzglbmfzr` | 矩阵管理部门负责人 | `varchar2` | 4000 | 是 | 矩阵管理部门负责人 |
| 16 | `jzglbmfgld` | 矩阵管理部门分管领导 | `varchar2` | 4000 | 是 | 矩阵管理部门分管领导 |
| 17 | `bmfzr` | 矩阵部门负责人员 | `varchar2` | 4000 | 是 | 矩阵部门负责人员 |
| 18 | `bmfgld` | 矩阵部门分管领导 | `varchar2` | 4000 | 是 | 矩阵部门分管领导 |
| 19 | `outkey` | 外键 | `varchar2` | 800 | 是 | 和其他系统集成同步时使用 |
| 20 | `budgetatuomoveorder` | 做预算结转时的临时排序用 | `integer` | - | 是 | 做预算结转时的临时排序用 |
| 21 | `ecology_pinyin_search` | 部门首字母搜索 | `varchar2` | 1000 | 是 | 部门首字母搜索使用 |
| 22 | `tlevel` | 部门层级 | `integer` | - | 是 | 组织图表显示时使用 |
| 23 | `created` | 创建时间 | `timestamp(6)` | 11 | 是 | 创建时间 |
| 24 | `creater` | 创建人 | `integer` | - | 是 | 创建人 |
