/**
 * 泛微 Ecology 9 知识文档创建与富文本处理实战脚本 (Node.js)
 * 涵盖流程：
 * 1. 查询文档分类目录
 * 2. 创建包含 HTML 富文本内容的知识文档 (accForDoc / HTML 内容)
 * 3. 读取文档的 HTML 详情数据
 */

const EcologyClient = require('../scripts/ecology_token_client');

const client = new EcologyClient({
  baseUrl: 'http://oa.yourcompany.com:8088',
  appId: 'KNOWLEDGE_DEV_01',
  defaultUserId: '1'
});

async function runDocDemo() {
  try {
    console.log('=== 1. 创建一篇新的知识文档 ===');
    const createDocRes = await client.request({
      path: '/api/doc/save/accForDoc',
      method: 'POST',
      data: {
        docsubject: `产品上线通知公告 - ${new Date().toLocaleDateString()}`,
        seccategory: '15', // 二级目录ID
        doccontent: '<h2>系统升级维护完成通知</h2><p>本次升级已全面适配 E9 开放平台接口，服务正常运行中。</p>',
        doccreaterid: '1'  // 创建人ID
      }
    });
    console.log('创建文档结果:', JSON.stringify(createDocRes, null, 2));

    console.log('\n=== 2. 获取文档列表 ===');
    const docListRes = await client.request({
      path: '/api/doc/out/more/list',
      method: 'POST',
      data: {
        pageNo: '1',
        pageSize: '5'
      }
    });
    console.log('最新文档列表:', JSON.stringify(docListRes, null, 2));

  } catch (err) {
    console.error('文档接口调用异常:', err);
  }
}

runDocDemo();
