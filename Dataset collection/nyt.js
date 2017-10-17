request.get({
  url: "https://api.nytimes.com/svc/archive/v1/2016/1.json",
  qs: {
    'api-key': "20fbb215e7d1461492487529241dd216"
  },
}, function(err, response, body) {
  body = JSON.parse(body);
  console.log(body);
})	