var appVersion='ecoway-0.1';
var appEvents = {};
_.extend(appEvents, Backbone.Events);


var BaseMethods = {
    debugMode:true,
    baseListeners:function(){
        var me=this;
        me.listenTo(appEvents, "Log", me.onLog);
    },
    onLog:function(messageLog){
        var me=this;
        console.log("Message");
        if(me.debugMode){
            console.log(messageLog);
        }
    }
};// views//a-999-main.js


var MainView = Backbone.View.extend({
        el: $('body'),
        initialize: function(opts){
            var me =this;
            _.extend(this,BaseMethods); 
            _.extend(this,opts);
			this.template = _.template("");
            me.listenTo(appEvents,"zoomPosition", me.onZoomPosition);            
        },                    
        onZoomPosition:function(){
            var me=this;
                 
        },
	    render: function() {
	        var me=this;
	        return me;
	    }
    });


// views//a-999-main.js
