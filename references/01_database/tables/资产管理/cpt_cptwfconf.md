# 泛微OA 数据表: `cpt_cptwfconf`

- **所属模块**: `资产管理`
- **数据库表名**: `cpt_cptwfconf`
- **字段总数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `cptno` | 资产编号 | `varchar2` | 800 | 是 | - |
| 2 | `zclx` | 资产类型 | `integer` | - | 是 | - |
| 3 | `rkrq` | 入库日期 | `varchar2` | 80 | 是 | - |
| 4 | `ssbm` | 所属部门 | `integer` | - | 是 | - |
| 5 | `formid` | 流程表单 | `integer` | - | 是 | - |
| 6 | `creater` | 创建人 | `integer` | - | 是 | - |
| 7 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 8 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 9 | `lastmoddate` | 修改日期 | `char` | 10 | 是 | - |
| 10 | `lastmodtime` | 修改时间 | `char` | 8 | 是 | - |
| 11 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 12 | `wftype` | 流程类型 | `varchar2` | 160 | 是 | 流程类型 |
| 13 | `wfid` | 流程id | `integer` | - | 是 | 流程id |
| 14 | `sqr` | 申请人 | `integer` | - | 是 | 申请人 |
| 15 | `zczl` | 资产资料 | `integer` | - | 是 | 资产资料 |
| 16 | `zc` | 资产 | `integer` | - | 是 | 资产 |
| 17 | `sl` | 数量 | `integer` | - | 是 | 数量 |
| 18 | `zcz` | 资产组 | `integer` | - | 是 | 资产组 |
| 19 | `jg` | 价格 | `integer` | - | 是 | 价格 |
| 20 | `rq` | 日期 | `integer` | - | 是 | 日期 |
| 21 | `ggxh` | 规格型号 | `integer` | - | 是 | 规格型号 |
| 22 | `cfdd` | 存放地点 | `integer` | - | 是 | 存放地点 |
| 23 | `bz` | 备注 | `integer` | - | 是 | 备注 |
| 24 | `wxqx` | 维修期限 | `integer` | - | 是 | 维修期限 |
| 25 | `wxdw` | 维修单位 | `integer` | - | 是 | 维修单位 |
| 26 | `isasync` | 是否异步提交 | `integer` | - | 是 | 是否异步提交(预留字段,暂未开放使用) |
| 27 | `actname` | action动作名称 | `varchar2` | 1000 | 是 | action动作名称 |
