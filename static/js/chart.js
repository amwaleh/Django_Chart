
var type = 'bar'; // Set default chart as Bar chart
var vector = ['line', 'radar']; // graphs that need one color
var myChart;

// Function for retreiving data and populating the chart
function findData() {
    $.ajax({
            method: 'GET',
            url: '/graph/',
            cache: false,
            success: function (res) {
                var ctx = document.getElementById("myChart");
                myChart = new Chart(ctx, {
                    type: type || 'bar',
                    data: {
                        labels: res.labels,
                        datasets: [{
                            label: 'population',
                            data: res.data,
                            backgroundColor: vector.includes(type) ? res.color[0] : res.color
                        }
                        ]},
                        options: {
                            title: {
                                display: true,
                                text: res.title,
                            },
                            legends :{
                                display: false
                            }
                        }
                    });
            },
            error: function (err) {
                console.log(err);
            }
        }
    );
};

// Handle click event
$('.graph-type').on('click', 'button', function () {
    myChart.destroy();
    type = this.name;
    findData();
});

// Auto generate the graph when page is loaded
findData();
