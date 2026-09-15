# 泛微OA 数据表: `crm_sectorinfo`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_sectorinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `fullname` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `description` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 4 | `parentid` | 上一级行业 | `integer` | - | 是 | 上一级行业 |
| 5 | `seclevel` | 行业级别 | `integer` | - | 是 | 没有parent的为0，然后根据parent+1来确定 |
| 6 | `sectors` | 区域 | `varchar2` | 1000 | 是 | 区域 |
| 7 | `orderkey` | 排序字段 | `integer` | - | 是 | 排序字段 |
