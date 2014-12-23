function getMeeting(){
    
    var terms = $('#timedropdown').val();
    var near ="Columbia University";

    var message= {
        action : 'http://api.nytimes.com/svc/community/v2/comments/random.jsonp?api-key=6715295fd984ee301ef2ec74e01e6ff6:10:70159746'
    }

    $.ajax({
    'url': message.action,
    'type': 'GET',
    'dataType': 'jsonp',
    'cache':true,
    'success': function(data,textStats,XMLHttpRequest){
        var output = prettyPrint(data);

        var status = data['status'];
        var copyright = data['copyright'];
        var total_no_of_comments = data['results']['totalCommentsReturned'];
        var comment_one = data['results']['comments']['commentBody'];
        
        }

    });

$('#box').show();

}