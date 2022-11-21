const express = require('express');
const bodyparser = require('body-parser');
const cors = require('cors');
const config = require('../backendserver/config/db.config');

//create express app
const app = express();

//setup server port
// const port = process.env.PORT || 3000;
port = 3000;

const path = require('path');

app.use(cors());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }));
//parse requests of content-type - application/json
app.use(bodyparser.json());

app.use(express.json());


app.get('/api/student', (req, res) => {
    console.log("Posting new user!");
    res.send("Hello!");
});

app.post('/api/student', (req, res) => {
    console.log("trying to sign in a new user");
    res.send("Hello!");
});




//require user routes
const userRoutes = require('./routes/user.route');

//using as middleware
app.use('/student', userRoutes);







// app.use(express.static(__dirname + '../src/index.html'));
// app.get('/', (req, res) => {

//     res.sendFile(path.join(__dirname, '../src/index.html'));

// });

//get all data
app.get('/student', (req, res) => {
    let sql = "select * from student";
    config.query(sql, (err, results) => {

        if (err) throw err;
        res.send(results);
    });
    // res.send('Hey there!');
});

// insert data
/*app.post('/student', (req, res) => {
    console.log(req.body);
    let fName = req.body.firstname;
    let lName = req.body.lastname;
    let email = req.body.email;
    let password = req.body['password '];
    let sql = `INSERT INTO student(firstname,lastname,email,password) VALUES ("${fName}","${lName}","${email}","${password}")`;
    config.query(sql, (err, results) => {
        if (err) throw err;
        res.send(results);
    });

});*/


// app.post('/user_signup', (req, res) => {
//     let fName = "che";
//     let lName = "tna";
//     let email = "chetna@gmail.com";
//     let password = "1234";
//     let sql = `INSERT INTO user_signup(firstname,lastname,email,password) VALUES ("${fName}","${lName}","${email}","${password}")`;
//     config.query(sql, (err, results) => {
//         if (err) throw err;
//         res.send(results);
//     });

// });



// Import our own modules
const flagsModule = require("./../../flags/flags");
const coursesModule = require("./../../courses/courses");
const examsModule = require("./../../exams/exams");
const loginModule = require("./../../login/login");
const searchModule = require("./../../search/search");
const wishlistModule = require("./../../wishlist/wishlist");
// const categoryModule = require("./../../category/category");
const databaseModule = require("./../../databaseManager/database_manager");

flagsObj = new flagsModule.Flags();
coursesObj = new coursesModule.Courses();
examsObj = new examsModule.Exams();
loginObj = new loginModule.Login();
searchObj = new searchModule.Search();
wishlistObj = new wishlistModule.Wishlist();
// categoryObj = new categoryModule.Category();
databaseObj = databaseModule.databaseManager;

//define a root route
app.get('/', (req, res) => {
    res.send("Hello World!");
});


/* app.post("/student", (req, res) => {
    console.log(req.body);
    loginObj.verifyCredentials((user) => {
        res.send(user);
    });
});*/

/*app.post("/student", (req, res) => {
    console.log(req.body);
    loginObj.addNewUser((newStudent) => {
        res.send(newStudent);

    });

});*/
app.get("/flags", (req, res) => {
    flagsObj.getFlaggedCourses(function(courseObjects) {
        res.send(courseObjects);
    });
});

app.get("/flags/new", (req, res) => {
    course_id = req.query.course_id;
    console.log(req.query);
    flagsObj.flagCourse(course_id, function() {
        res.send("{}");
    });
});

app.post("/flags/delete", (req, res) => {
    console.log(req.body.courseId);
    flagsObj.deleteCourse(req.body.courseId, function() {
        res.send("{}");
    });
});

app.get("/wishlist", (req, res) => {
    wishlistObj.getWishlistCourses(1, function(results) {
        res.send(results);
    });
});

app.get("/wishlist/add", (req, res) => {
    course_id = parseInt(req.query.course_id);
    wishlistObj.addToWishlist(course_id, 1, function() {
        res.send("{}");
    });
});

app.get("/courses", (req, res) => {
    coursesObj.getAllCourses(function(results) {
        res.send(results);
    });
});

app.get("/search", (req, res) => {
    query = req.query.query;
    res.send(searchObj.searchClasses(query));
});

// app.get("/categoryList", (req, res) => {
//     categoryObj.getAllCategory(function(categories){
//         res.send(categories);
//     });
// });

app.post("/courses/new", (req, res) => {
    console.log("In courses/new");
    console.log(req.body);
    req.body.title = req.body.nameofcourse;
    req.body.category = 1;
    //req.body.description = req.body.keywords;
    req.body.instructor_id = 1;
    coursesObj.addNewCourse(req.body, function() {
        res.send("True");
    });
});

app.post("/student", (req, res) => {
    console.log(req.body);
    req.body.first_name = req.body.firstname
    req.body.last_name = req.body.lastname
    req.body.password = req.body["password "]
    loginObj.addNewUser(req.body, (newStudent) => {
        res.send("True");
    });
});

app.post("/login", (req, res) => {
    console.log(req.body);
    loginObj.verifyCredentials(req.body.email, req.body.password, function(retu) {
        res.send(retu);
    });
});


app.post("/send_comment", (req, res) => {
    console.log(req.body);
    if (req.body.reply != undefined) {
        req.body.reply = req.body.reply.replace("'", "");
    }
    databaseObj.addDiscussion(1, req.body.reply);
    console.log("Finished posting to the database.");
    res.send("OK");
});

app.get("/get_comments", (req, res) => {
    databaseObj.getDiscussion(1, function(results) {
        res.send(results);
    });
});

app.post("/user/update", (req, res) => {
    console.log(req.body);
    res.send("{}");
});

// app.post("/send_comment", (req, res) => {
//   console.log(req.body);
//   // console.log(val);
//   databaseObj.addDiscussion();


// });

app.get('/api/send_comment', (req, res) => {
  console.log("Posting new comment!");
  res.send("Hello!");
});


addModules = function(courseId, moduleObjList, callback) {
    if (moduleObjList.length == 0) {
        callback();
    } else {
        thisModule = moduleObjList[0];
        moduleObjList.shift();
        databaseObj.addCourseModule(courseId, thisModule.title, thisModule.video_link, thisModule.description, function() {
            addModules(courseId, moduleObjList, callback);
        });
    }
}

app.post("/course/addmodules", (req, res) => {
    modules = [];
    moduleObj = {};
    moduleObj.title = req.body.Title_1st_course;
    moduleObj.description = req.body.Description1;
    moduleObj.video_link = req.body.link_1st_course;
    modules.push(moduleObj);

    moduleObj2 = {};
    moduleObj2.title = req.body.Title_2nd_course;
    moduleObj2.description = req.body.Description2;
    moduleObj2.video_link = req.body.link_2nd_course;
    modules.push(moduleObj2);

    moduleObj3 = {};
    moduleObj3.title = req.body.Title_3rd_course;
    moduleObj3.description = req.body.Description3;
    moduleObj3.video_link = req.body.link_3rd_course;
    modules.push(moduleObj3);

    moduleObj4 = {};
    moduleObj4.title = req.body.Title_4th_course;
    moduleObj4.description = req.body.Description4;
    moduleObj4.video_link = req.body.link_4th_course;
    modules.push(moduleObj4);

    moduleObj5 = {};
    moduleObj5.title = req.body.Title_5th_course;
    moduleObj5.description = req.body.Description5;
    moduleObj5.video_link = req.body.link_5th_course;
    modules.push(moduleObj5);

    moduleObj6 = {};
    moduleObj6.title = req.body.Title_6th_course;
    moduleObj6.description = req.body.Description6;
    moduleObj6.video_link = req.body.link_6th_course;
    modules.push(moduleObj6);

    moduleObj7 = {};
    moduleObj7.title = req.body.Title_7th_course;
    moduleObj7.description = req.body.Description7;
    moduleObj7.video_link = req.body.link_7th_course;
    modules.push(moduleObj7);

    moduleObj8 = {};
    moduleObj8.title = req.body.Title_8th_course;
    moduleObj8.description = req.body.Description8;
    moduleObj8.video_link = req.body.link_8th_course;
    modules.push(moduleObj8);

    moduleObj9 = {};
    moduleObj9.title = req.body.Title_9th_course;
    moduleObj9.description = req.body.Description9;
    moduleObj9.video_link = req.body.link_9th_course;
    modules.push(moduleObj9);

    moduleObj10 = {};
    moduleObj10.title = req.body.Title_10th_course;
    moduleObj10.description = req.body.Description10;
    moduleObj10.video_link = req.body.link_10th_course;
    
    modules.push(moduleObj10);

    course_id = 1;
    addModules(course_id, modules, function() {
        res.send("{}");
    });
});

app.get("/course", (req, res) => {
    console.log(req.query);
    course_id = req.query.course_id;
    coursesObj.getCourseFromId(course_id, function(result) {
        res.send(result);
    });
});

app.post("/get_module", (req, res) => {
    console.log(req.query);
    course_id = req.query.course_id;    
    if (course_id == undefined) {
        course_id = 1;
    }
    coursesObj.getFullCourse(course_id, function(result) {
        res.send(result);
    });
});

app.get("/get_module", (req, res) => {
    console.log(req.query);
    course_id = req.query.course_id;    
    if (course_id == undefined) {
        course_id = 1;
    }
    coursesObj.getFullCourse(course_id, function(result) {
        res.send(result);
    });
});

app.listen(port, () => {
    console.log('server is running...');
    console.log(`listening on port ${port}!`);
});

