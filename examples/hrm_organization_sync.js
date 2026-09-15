/**
 * 泛微 Ecology 9 人力资源与组织架构同步实战脚本 (Node.js)
 * 涵盖流程：
 * 1. 查询 OA 分部与部门组织树
 * 2. 批量拉取/核对人员列表与状态
 * 3. 演示员工信息维护与组织关系关联
 */

const EcologyClient = require('../scripts/ecology_token_client');

const client = new EcologyClient({
  baseUrl: 'http://oa.yourcompany.com:8088',
  appId: 'HR_SYNC_SERVICE',
  defaultUserId: '1'
});

async function syncHrmDemo() {
  try {
    console.log('=== 1. 获取组织机构树 (分部/部门) ===');
    const orgTree = await client.request({
      path: '/api/hrm/org/tree',
      method: 'GET'
    });
    console.log('组织架构树响应概览:', typeof orgTree === 'object' ? Object.keys(orgTree) : orgTree);

    console.log('\n=== 2. 按条件查询人员花名册 ===');
    const userList = await client.request({
      path: '/api/hrm/res/list',
      method: 'POST',
      data: {
        pageNo: '1',
        pageSize: '10',
        status: '1' // 1 为在职正式员工
      }
    });
    console.log('在职人员查询结果:', JSON.stringify(userList, null, 2));

    console.log('\n=== 3. 获取特定员工详细卡片信息 ===');
    const targetUserId = '1';
    const userDetail = await client.request({
      path: '/api/hrm/resource/getResourceInfo',
      method: 'GET',
      params: { id: targetUserId }
    });
    console.log(`员工 [ID=${targetUserId}] 详情:`, JSON.stringify(userDetail, null, 2));

  } catch (err) {
    console.error('HRM 同步异常:', err);
  }
}

syncHrmDemo();
