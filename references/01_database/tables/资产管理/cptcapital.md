# 泛微OA 数据表: `cptcapital`

- **所属模块**: `资产管理`
- **数据库表名**: `cptcapital`
- **字段总数**: `68`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `mark` | 编号 | `varchar2` | 480 | 是 | 编号 |
| 3 | `name` | 名称 | `varchar2` | 480 | 是 | 名称 |
| 4 | `barcode` | 条形码 | `varchar2` | 240 | 是 | 条形码 |
| 5 | `startdate` | 生效日 | `char` | 10 | 是 | 生效日 |
| 6 | `enddate` | 生效至 | `char` | 10 | 是 | 生效至 |
| 7 | `seclevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 8 | `costcenterid` | 成本中心id | `integer` | - | 是 | 成本中心id |
| 9 | `crmid` | 客户id | `integer` | - | 是 | 客户id |
| 10 | `sptcount` | 是否单独核算 | `char` | 1 | 是 | (0:否1:是) |
| 11 | `capitalcost` | 成本 | `number` | (18,2) | 是 | 成本 |
| 12 | `startprice` | 开始价格 | `number` | (18,2) | 是 | 开始价格 |
| 13 | `depreendprice` | 备用字段 | `number` | (18,2) | 是 | 备用字段 |
| 14 | `capitalspec` | 规格型号 | `varchar2` | 480 | 是 | 规格型号 |
| 15 | `capitallevel` | 资产等级 | `varchar2` | 240 | 是 | 资产等级 |
| 16 | `manufacturer` | 制造厂商 | `varchar2` | 800 | 是 | 制造厂商 |
| 17 | `manudate` | 出厂日期 | `char` | 10 | 是 | 出厂日期 |
| 18 | `capitaltypeid` | 资产类型 | `integer` | - | 是 | 资产类型 |
| 19 | `currentnum` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 20 | `capitalgroupid` | 资产组 | `integer` | - | 是 | 资产组 |
| 21 | `attribute` | 属性 | `integer` | - | 是 | 属性 |
| 22 | `unitid` | 计量单位 | `integer` | - | 是 | 计量单位 |
| 23 | `blongdepartment` | 所属部门 | `integer` | - | 是 | 所属部门 |
| 24 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 25 | `resourceid` | 使用人(资料管理员) | `integer` | - | 是 | 使用人(资料管理员) |
| 26 | `customerid` | 供应商id | `integer` | - | 是 | 供应商id |
| 27 | `replacecapitalid` | 替代 | `integer` | - | 是 | 替代 |
| 28 | `isinner` | 帐内帐外 | `integer` | - | 是 | 1,帐内;2,帐外; |
| 29 | `currencyid` | 币种 | `integer` | - | 是 | 币种 |
| 30 | `remark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 31 | `version` | 版本 | `varchar2` | 480 | 是 | 版本 |
| 32 | `itemid` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 33 | `capitalimageid` | 资产图片id | `integer` | - | 是 | 资产图片id |
| 34 | `depremethod1` | 折旧法一 | `integer` | - | 是 | 折旧法一 |
| 35 | `depremethod2` | 折旧法二 | `integer` | - | 是 | 折旧法二 |
| 36 | `deprestartdate` | 折旧开始日期 | `char` | 10 | 是 | 折旧开始日期 |
| 37 | `depreenddate` | 折旧结束日期 | `char` | 10 | 是 | 折旧结束日期 |
| 38 | `stateid` | 状态 | `integer` | - | 是 | 状态 |
| 39 | `location` | 存放地点 | `varchar2` | 800 | 是 | 存放地点 |
| 40 | `usedhours` | 备用字段 | `number` | (18,3) | 是 | 备用字段 |
| 41 | `createrid` | 创建者id | `integer` | - | 是 | 创建者id |
| 42 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 43 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 44 | `lastmoderid` | 更新人id | `integer` | - | 是 | 更新人id |
| 45 | `lastmoddate` | 更新日期 | `char` | 10 | 是 | 更新日期 |
| 46 | `lastmodtime` | 更新时间 | `char` | 8 | 是 | 更新时间 |
| 47 | `isdata` | 资产资料或者资产 | `char` | 1 | 是 | （1:资产资料,2:资产） |
| 48 | `datatype` | 所属资产资料id | `integer` | - | 是 | 所属资产资料id |
| 49 | `relatewfid` | 入库的工作流id | `integer` | - | 是 | 入库的工作流id |
| 50 | `fnamark` | 财务编号 | `varchar2` | 480 | 是 | 财务编号 |
| 51 | `alertnum` | 预警数量 | `number` | (18,2) | 是 | 预警数量 |
| 52 | `counttype` | 备用字段 | `char` | 1 | 是 | 备用字段 |
| 53 | `invoice` | 发票号码 | `varchar2` | 640 | 是 | 发票号码 |
| 54 | `stockindate` | 入库日期 | `char` | 10 | 是 | 入库日期 |
| 55 | `depreyear` | 折旧年限 | `number` | (18,2) | 是 | 折旧年限 |
| 56 | `deprerate` | 残值率真 | `number` | (18,2) | 是 | 残值率真 |
| 57 | `selectdate` | 购置日期 | `char` | 10 | 是 | 购置日期 |
| 58 | `olddepartment` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 59 | `frozennum` | 冻结数量 | `number` | (15,2) | 是 | 冻结数量 |
| 60 | `blongsubcompany` | 所属分部 | `integer` | - | 是 | 所属分部 |
| 61 | `issupervision` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 62 | `amountpay` | 备用字段 | `number` | (18,2) | 是 | 备用字段 |
| 63 | `purchasestate` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 64 | `contractno` | 合同号 | `varchar2` | 800 | 是 | 合同号 |
| 65 | `equipmentpower` | 备用字段 | `varchar2` | 800 | 是 | 备用字段 |
| 66 | `topassortmentid` | 顶级资产组 | `integer` | - | 是 | 顶级资产组 |
| 67 | `capitalnum` | 资产数量 | `number` | (18,2) | 是 | 资产数量 |
| 68 | `ecology_pinyin_search` | 联想输入简拼 | `varchar2` | 1000 | 是 | 联想输入简拼 |
