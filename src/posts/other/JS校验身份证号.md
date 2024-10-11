---
date: 2023-06-16
category:
    - javascript
tag:
    - javascript
    - 前端
    - ecmascript-6
    - html5
---
 # JS校验身份证号
> 原文链接: [ js最全身份证号码校验 ]()
    
    
    function validateIdCard (idCard) {
        let vcity = {
            11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古",
            21: "辽宁", 22: "吉林", 23: "黑龙江", 31: "上海", 32: "江苏",
            33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东", 41: "河南",
            42: "湖北", 43: "湖南", 44: "广东", 45: "广西", 46: "海南", 50: "重庆",
            51: "四川", 52: "贵州", 53: "云南", 54: "西藏", 61: "陕西", 62: "甘肃",
            63: "青海", 64: "宁夏", 65: "新疆", 71: "台湾", 81: "香港", 82: "澳门", 91: "国外"
        };
        //是否为空
        if (idCard === "") {
            return false;
        }
        //校验长度，类型
        if (isCardNo(idCard) === false) {
            return false;
        }
        //检查省份
        if (checkProvince(idCard, vcity) === false) {
            return false;
        }
        //校验生日
        if (checkBirthday(idCard) === false) {
            return false;
        }
        //检验位的检测
        if (checkParity(idCard) === false) {
            return false;
        }
        return true;
    }
    
    
    // 校验号码长度、类型
    function isCardNo (card) {
        // 身份证号码为15位或者18位，
        // 15位时全为数字，18位前17位为数字，
        // 最后一位是校验位，可能为数字或字符X
        let reg = /(^\d{15}$)|(^\d{17}(\d|X|x)$)/;
        return reg.test(card)
    }
    
    
    // 校验省份，取号码前两位
    function checkProvince (card, vcity) {
        let province = card.substr(0, 2);
        if (vcity[province] == undefined) {
            return false;
        }
        return true;
    }
    
    
    // 校验日期
    function verifyBirthday (year, month, day, birthday) {
        let date = new Date();
        // 校验年月日
        if (birthday.getFullYear() == year
            && (birthday.getMonth() + 1) == month
            && birthday.getDate() == day) {
            // 判断年份的范围（0岁到100岁)
            let time = date.getFullYear() - year;
            if (time >= 0 && time <= 100) {
                return true;
            }
            return false;
        }
        return false;
    }
    
    
    // 校验生日
    function checkBrithday (card) {
        let len = card.length;
        // 身份证15位时，
        // 次序为省（3位）市（3位）年（2位）月（2位）日（2位）校验位（3位），
        // 皆为数字
        if (len == "15") {
            let re_fifteen = /^(\d{6})(\d{2})(\d{2})(\d{2})(\d{3})$/;
            let arr_data = card.match(re_fifteen);
            let year = arr_data[2];
            let month = arr_data[3];
            let day = arr_data[4];
            let birthday = new Date("19" + year + '/' + month + '/' + day);
            return verifyBirthday("19" + year, month, day, birthday);
        }
        // 身份证18位时，
        // 次序为省（3位）市（3位）年（4位）月（2位）日（2位）校验位（4位），
        // 校验位末尾可能为X
        if (len == "18") {
            let re_eighteen = /^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X|x)$/;
            let arr_data = card.match(re_eighteen);
            let year = arr_data[2];
            let month = arr_data[3];
            let day = arr_data[4];
            let birthday = new Date(year + '/' + month + '/' + day);
            return verifyBirthday(year, month, day, birthday);
        }
        return false;
    }
    
    
    // 15位转18位身份证号
    function changeFiveteenToEighteen (card) {
        if (card.length == "15") {
            let arrInt = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2];
            let arrCh = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"];
            let cardTemp = 0, i;
            card = card.substr(0, 6) + "19" + card.substr(6, card.length - 6);
            for (i = 0; i < 17; i++) {
                cardTemp += card.substr(i, 1) * arrInt[i];
            }
            card += arrCh[cardTemp % 11];
            return card;
        }
        return card;
    }
    
    
    // 检测校验位
    function checkParity (card) {
        // 15位转18位
        card = changeFiveteenToEighteen(card);
        let len = card.length;
        if (len == "18") {
            let arrInt = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2];
            let arrCh = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"];
            let cardTemp = 0, i, valnum;
            for (i = 0; i < 17; i++) {
                cardTemp += card.substr(i, 1) * arrInt[i];
            }
            valnum = arrCh[cardTemp % 11];
            if (valnum == card.substr(17, 1).toLocaleUpperCase()) {
                return true;
            }
            return false;
        }
        return false;
    }

