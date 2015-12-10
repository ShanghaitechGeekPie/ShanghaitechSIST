function RefreshTreeNode(id){
	zTreeObj.reAsyncChildNodes(zTreeObj.getNodeByTId(id),"refresh",false)
}
function ChangeTreeNode(id){
	zTreeObj.getNodeByTId(id).click();
}
function ChangeTableNode(id){
	TableObj.clear().draw();
	$.ajax({
		url: "/dashboard/datacontrol/?request=GetNodes&id="+id,
		success: function(data){
			TableObj.rows.add(data).draw();
		},
		dataType: 'json'
	});
	TableObj.draw();
}
function ChangeNode(id){
	ChangeTreeNode(id);
	ChangeTableNode(id);
}
var zTreeObj;
var TableObj;
var setting = {
	// treeId : "",
	// treeObj : null,
	async : {
		autoParam : ['id'],
		// contentType : "application...",
		// dataFilter : null,
		// dataType : "text",
		enable : true,
		otherParam: {"request":"GetKeyNodes"},
		type : "get",
		url : "/dashboard/datacontrol/"
	},
	callback : {
		// beforeAsync : null,
		// beforeCheck : null,
		beforeClick : function(treeId, treeNode, clickFlag){
			// alert("beforeClick " + treeId + treeNode + clickFlag)
		},
		// beforeCollapse : null,
		beforeDblClick : function(treeId, treeNode){
			// alert("beforeClick " + treeId + treeNode)
		},
		// beforeDrag : null,
		// beforeDragOpen : null,
		// beforeDrop : null,
		// beforeEditName : null,
		// beforeExpand : null,
		// beforeMouseDown : null,
		// beforeMouseUp : null,
		// beforeRemove : null,
		// beforeRename : null,
		// beforeRightClick : null,
		// onAsyncError : null,
		// onAsyncSuccess : null,
		// onCheck : null,
		onClick : function(event, treeId, treeNode, clickFlag){
			// alert("onClick " + event + treeId + treeNode + clickFlag)
			zTreeObj.expandNode(treeNode,true);
			ChangeTableNode(treeNode.id);
		},
		// onCollapse : null,
		onDblClick : function(treeId, treeNode){
			return treeNode.level > 0;
		},
		// onDrag : null,
		// onDragMove : null,
		// onDrop : null,
		// onExpand : null,
		// onMouseDown : null,
		// onMouseUp : null,
		// onNodeCreated : null,
		// onRemove : null,
		// onRename : null,
		// onRightClick : null
	},
	// check : {
	// 	autoCheckTrigger : false,
	// 	chkboxType : {"Y": "ps", "N": "ps"},
	// 	chkStyle : "checkbox",
	// 	enable : false,
	// 	nocheckInherit : false
	// 	chkDisabledInherit : false
	// 	radioType : "level"
	// },
	data : {
		keep : {
			leaf : true,
			parent : true
		},
		// key : {
		// 	checked : "checked",
		// 	children : "children",
		// 	name : "name",
		// 	title : ""
		// 	url : "url"
		// },
		simpleData : {
			enable : true,
			idKey : "id",
			pIdKey : "pId",
			rootPId : 0
		}
	},
	// edit : {
	// 	drag : {
	// 		autoExpandTrigger : true,
	// 		isCopy : true,
	// 		isMove : true,
	// 		prev : true,
	// 		next : true,
	// 		inner : true,
	// 		borderMax : 10,
	// 		borderMin : -5,
	// 		minMoveSize : 5,
	// 		maxShowNodeNum : 5,
	// 		autoOpenTime : 500
	// 	},
	// 	editNameSelectAll : false,
	// 	enable : false,
	// 	removeTitle : "remove",
	// 	renameTitle : "rename",
	// 	showRemoveBtn : true,
	// 	showRenameBtn : true
	// },
	view : {
	// 	addDiyDom : null,
	// 	addHoverDom : null,
	// 	autoCancelSelected : true,
		dblClickExpand : false,
	// 	expandSpeed : "fast",
	// 	fontCss : {},
	// 	nameIsHTML : false,
	// 	removeHoverDom : null,
	// 	selectedMulti : true,
	// 	showIcon : true,
	// 	showLine : true,
	// 	showTitle : true,
	// 	txtSelectedEnable : false
	}
}

var zNodes =[
	{id:0, name:"根 Root", open:false, isParent:true},
];

// zTree 的数据属性，深入使用请参考 API 文档（zTreeNode 节点数据详解）\
$(document).ready(function(){
  zTreeObj = $.fn.zTree.init($("#node_tree"), setting,zNodes);
  var t=zTreeObj.getNodeByParam("id",0);
});

$(document).ready(function() {
   TableObj = $('#example').DataTable();
} );