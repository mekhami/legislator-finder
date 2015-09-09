var gulp = require('gulp'),
    sass = require('gulp-ruby-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'),
    jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),
    imagemin = require('gulp-imagemin'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat'),
    notify = require('gulp-notify'),
    cache = require('gulp-cache'),
    livereload = require('gulp-livereload'),
    del = require('del');

gulp.task('styles', function() {
    return sass('politics/finder/static/scss/main.scss', { style: 'expanded' })
        .pipe(autoprefixer('last 2 version'))
        .pipe(gulp.dest('static/css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('static/css'))
        .pipe(notify({ message: 'Styles task complete' }));
    });

gulp.task('bootstrap', function() {
    gulp.src('bower_components/jquery/dist/jquery.min.js')
        .pipe(gulp.dest('static/js'))
    return gulp.src('bower_components/bootstrap/dist/**/*')
        .pipe(gulp.dest('static/'))
});

gulp.task('scripts', function() {
   return gulp.src('politics/*/static/**/*.js')
        .pipe(jshint('.jshintrc'))
        .pipe(jshint.reporter('default'))
        .pipe(concat('main.js'))
        .pipe(gulp.dest('static/js'))
        .pipe(rename({suffix: '.min'}))
        .pipe(uglify())
        .pipe(gulp.dest('static/js'))
        .pipe(notify({ message: 'Scripts task complete' }));
    });

gulp.task('images', function() {
    return gulp.src('politics/*/static/images/*')
        .pipe(cache(imagemin({ optimizationLevel: 5, progressive: true, interlaced: true })))
        .pipe(gulp.dest('politics/src/assets/images'))
        .pipe(notify({ message: 'Images task complete' }));
    });

gulp.task('clean', function(cb) {
    del(['static/css', 'static/js', 'politics/src/assets/images'], cb)
    });

gulp.task('default', ['clean'], function() {
    gulp.start('styles', 'scripts', 'images', 'bootstrap');
    });

gulp.task('watch', function() {
    gulp.watch('politics/*/static/**/*.scss', ['styles']);
    gulp.watch('politics/*/static/**/*.js', ['scripts']);
    gulp.watch('politics/*/static/images/*', ['images']);
    });
