import axios from 'axios';
import { useState } from 'react';
import { useFormContext } from 'react-hook-form';

import styles from '../register.module.scss'

const CheckLicense = () => {
    const { register, getValues, setValue } = useFormContext();
    const checkLicense = () => {
        const serviceKey = 'o2WKfqiR0FpPaO2or6Co%2FKtbTLzkTNC6yEpFGdlR7hlq8aqMTs8wFIS%2FoziOg31GuMz0qhiWDgBZgCcwAThSBg%3D%3D';
        axios.post(`https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey=${serviceKey}`, 
            {
                "b_no" : [`${getValues("license")}`]
            }
        )
        .then(function (res) {
            if (res.data.match_cnt > 0) {
                setValue("license" , getValues("license"))
            } else {
                alert(res.data.data[0].tax_type);
            }
        })
        .catch(function (err) {  
            console.log(err);
        });
    }
  
    return (
        <div className={styles.btnWrap}>
            <div className={styles.inputWrap}>
                <input type="text" placeholder="사업자등록 번호를 입력해 주세요." {...register("license", {required: true})} />
            </div>

            <button type="button" className={styles.btn} onClick={checkLicense}>인증하기</button>
        </div>
    )
  }

export default CheckLicense;
