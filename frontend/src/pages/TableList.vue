<template>
  <div>
       <div>
           <b-form-group label="교육용 요금제" icon="tim-icons icon-bulb-63">  
           <!-- <b-form-checkbox-group id="checkbox-group-2" v-model="selected" name="flavour-2">
               <b-form-checkbox value="graph-check">그래프 보기</b-form-checkbox>
              <b-form-checkbox value="info-check">수치 정보 보기</b-form-checkbox>
            </b-form-checkbox-group> -->
          </b-form-group>
        </div>
    
      <b-row align-v="stretch">
        <b-col cols="12" md="10">
          <b-row>
            <b-col cols="6">
              <b-row>
                <b-col sm="3">시작 일자</b-col>
                <b-col sm="7"> <b-input-group class="mb-3">
            <b-form-input
              id="example-input"
              v-model="value"
              type="text"
              placeholder="YYYY-MM-DD"
              autocomplete="off"
            ></b-form-input>
            <b-input-group-append>
              <b-form-datepicker
                v-model="value"
                button-only
                right
                locale="en-US"
                aria-controls="example-input"
                @context="onContext"
              ></b-form-datepicker>
            </b-input-group-append>
          </b-input-group>
      </b-col>
              </b-row>
            </b-col>
            <b-col cols="6">
               <b-row>
                <b-col sm="3">요금제 조회</b-col>
                <b-col sm="7"> 
                <b-form-select v-model="select" :options="options" > </b-form-select> 
                <!-- <el-select class="select-danger"
                   placeholder="요금제 선택"
                   v-model="selects.simple">
                 <el-option v-for="option in selects.languages"
                   class="select-danger"
                   :value="option.value"
                   :label="option.label"
                   :key="option.label">
                 </el-option
                </el-select
            <div class="mt-3"> <strong> {{select}} </strong> </div> 
            <b-input-group class="mb-3">
            <b-form-input
              id="example-input"
              v-model="value"
              type="text"
              placeholder="YYYY-MM-DD"
              autocomplete="off"
            ></b-form-input>
            <b-input-group-append>
              <b-form-datepicker
                v-model="value"
                button-only
                right
                locale="en-US"
                aria-controls="example-input"
                @context="onContext"
              ></b-form-datepicker>
            </b-input-group-append>
          </b-input-group>-->
     </b-col>
              </b-row>
            </b-col>
          </b-row>
          <b-row>
            <b-col cols="6">
              <b-row>
                <b-col sm="3">종료 일자</b-col>
                <b-col sm="7"> <b-input-group class="mb-3">
            <b-form-input
              id="example-input"
              v-model="value"
              type="text"
              placeholder="YYYY-MM-DD"
              autocomplete="off"
            ></b-form-input>
            <b-input-group-append>
              <b-form-datepicker
                v-model="value"
                button-only
                right
                locale="en-US"
                aria-controls="example-input"
                @context="onContext"
              ></b-form-datepicker>
            </b-input-group-append>
          </b-input-group>
     </b-col>
              </b-row>
            </b-col>
            <b-col cols="6">
               <b-row>
                <b-col sm="3">단위 선택</b-col>
                <b-col sm="7"> <b-form-group>
                  <b-form-radio-group 
                    v-model="selected2"
                    :options="option2"
                    name="radio-inline"
                  ></b-form-radio-group>
                 <!-- <base-radio inline name="radio1" class="mb-3" v-model="radio.radio1">연간</base-radio>
                  <base-radio inline name="radio2" class="mb-3" v-model="radio.radio1">월간</base-radio>
                  <base-radio inline name="radio3" class="mb-3" v-model="radio.radio1">일간</base-radio>-->
                </b-form-group>
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </b-col>
        <b-col cols="12" md="2">
            <b-button size="lg" variant="primary" style="height:60%;width:60%" >조회</b-button>
        </b-col>
          
      
      </b-row>
    <div class="row">
      <div class="col-12">
        <card type="chart">
          <template slot="header">
            <div class="row">
              <div class="col-sm-6" :class="isRTL ? 'text-right' : 'text-left'">
                <h5 class="card-category">{{$t('dashboard.totalShipments')}}</h5>
                <h2 class="card-title">{{$t('dashboard.performance')}}</h2>
              </div>
              <div class="col-sm-6">
                <div class="btn-group btn-group-toggle"
                     :class="isRTL ? 'float-left' : 'float-right'"
                     data-toggle="buttons">
                  <label v-for="(option, index) in bigLineChartCategories"
                         :key="option"
                         class="btn btn-sm btn-primary btn-simple"
                         :class="{active: bigLineChart.activeIndex === index}"
                         :id="index">
                    <input type="radio"
                           @click="initBigChart(index)"
                           name="options" autocomplete="off"
                           :checked="bigLineChart.activeIndex === index">
                    {{option}}
                  </label>
                </div>
              </div>
            </div>
          </template>
          <div class="chart-area">
            <line-chart style="height: 100%"
                        ref="bigChart"
                        chart-id="big-line-chart"
                        :chart-data="bigLineChart.chartData"
                        :gradient-colors="bigLineChart.gradientColors"
                        :gradient-stops="bigLineChart.gradientStops"
                        :extra-options="bigLineChart.extraOptions">
            </line-chart>
          </div>
        </card>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-4" :class="{'text-right': isRTL}">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category">{{$t('dashboard.totalShipments')}}</h5>
            <h3 class="card-title"><i class="tim-icons icon-bell-55 text-primary "></i> 763,215</h3>
          </template>
          <div class="chart-area">
            <line-chart style="height: 100%"
                        chart-id="purple-line-chart"
                        :chart-data="purpleLineChart.chartData"
                        :gradient-colors="purpleLineChart.gradientColors"
                        :gradient-stops="purpleLineChart.gradientStops"
                        :extra-options="purpleLineChart.extraOptions">
            </line-chart>
          </div>
        </card>
      </div>
      <div class="col-lg-4" :class="{'text-right': isRTL}">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category">{{$t('dashboard.dailySales')}}</h5>
            <h3 class="card-title"><i class="tim-icons icon-delivery-fast text-info "></i> 3,500€</h3>
          </template>
          <div class="chart-area">
            <bar-chart style="height: 100%"
                       chart-id="blue-bar-chart"
                       :chart-data="blueBarChart.chartData"
                       :gradient-stops="blueBarChart.gradientStops"
                       :extra-options="blueBarChart.extraOptions">
            </bar-chart>
          </div>
        </card>
        
        <card type="tasks" :header-classes="{'text-right': isRTL}">
          <template slot="header">
            <h6 class="title d-inline">{{$t('dashboard.tasks', {count: 5})}}</h6>
            <p class="card-category d-inline">{{$t('dashboard.today')}}</p>
            <base-dropdown menu-on-right=""
                           tag="div"
                           title-classes="btn btn-link btn-icon"
                           aria-label="Settings menu"
                           :class="{'float-left': isRTL}">
              <i slot="title" class="tim-icons icon-settings-gear-63"></i>
              <a class="dropdown-item" href="/">{{$t('dashboard.dropdown.action')}}</a>
              <a class="dropdown-item" href="/">{{$t('dashboard.dropdown.anotherAction')}}</a>
              <a class="dropdown-item" href="/">{{$t('dashboard.dropdown.somethingElse')}}</a>
            </base-dropdown>
          </template>
          <div class="table-full-width table-responsive">
            <task-list></task-list>
          </div>
        </card>
      </div>
      <div class="col-lg-6 col-md-12">
        <card class="card" :header-classes="{'text-right': isRTL}">
          <h4 slot="header" class="card-title">{{$t('dashboard.simpleTable')}}</h4>
          <div class="table-responsive">
            <user-table></user-table>
          </div>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
  import LineChart from '@/components/Charts/LineChart';
  import BarChart from '@/components/Charts/BarChart';
  import * as chartConfigs from '@/components/Charts/config';
  import TaskList from './Dashboard/TaskList';
  import UserTable from './Dashboard/UserTable';
  import config from '@/config';
  import { FormSelectPlugin } from 'bootstrap-vue';
 // import {Select, Option} from 'element-ui';
  export default {
    components: {
      LineChart,
      BarChart,
      TaskList,
      UserTable
      //[Select.name]: Select,
      //[Option.name]: Option
    },
    data() {
      return {
        select: null,
        options: [
          { value: null, text: '요금제 선택'  },
          { value: 'a', text: '교육용(갑) 저압전력' },
          { value: 'b', text: '교육용(갑) 고압A 선택I' },
          { value: 'c', text: '교육용(갑) 고압A 선택II' },
          { value: 'd', text: '교육용(갑) 고압B 선택I' },
          { value: 'e', text: '교육용(갑) 고압B 선택II' },
          { value: 'f', text: '교육용(을) 고압A 선택I' },
          { value: 'g', text: '교육용(을) 고압A 선택II' },
          { value: 'h', text: '교육용(을) 고압B 선택I' },
          { value: 'i', text: '교육용(을) 고압B 선택II' }
        ],
       /* selects: {
            simple: '',
            languages: [
              { value: 'a', label: '교육용(갑) 저압전력' },
              { value: 'b', label: '교육용(갑) 고압A 선택I' },
              { value: 'c', label: '교육용(갑) 고압A 선택II' },
              { value: 'd', label: '교육용(갑) 고압B 선택I' },
              { value: 'e', label: '교육용(갑) 고압B 선택II' },
              { value: 'f', label: '교육용(을) 고압A 선택I' },
              { value: 'g', label: '교육용(을) 고압A 선택II' },
              { value: 'h', label: '교육용(을) 고압B 선택I' },
              { value: 'i', label: '교육용(을) 고압B 선택II' }]
        },*/
        selected2: 'A',
        option2: [
          { value: 'A', text: '연간' },
          { value: 'B', text: '월간' },
          { value: 'C', text: '일간' }
        ],
        bigLineChart: {
          allData: [
            [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100],
            [80, 120, 105, 110, 95, 105, 90, 100, 80, 95, 70, 120],
            [60, 80, 65, 130, 80, 105, 90, 130, 70, 115, 60, 130]
          ],
          activeIndex: 0,
          chartData: {
            datasets: [{ }],
            labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
          },
          extraOptions: chartConfigs.purpleChartOptions,
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.4, 0],
          categories: []
        },
        purpleLineChart: {
          extraOptions: chartConfigs.purpleChartOptions,
          chartData: {
            labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
            datasets: [{
              label: "Data",
              fill: true,
              borderColor: config.colors.primary,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.primary,
              pointBorderColor: 'rgba(255,255,255,0)',
              pointHoverBackgroundColor: config.colors.primary,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [80, 100, 70, 80, 120, 80],
            }]
          },
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.2, 0],
        },
        greenLineChart: {
          extraOptions: chartConfigs.greenChartOptions,
          chartData: {
            labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV'],
            datasets: [{
              label: "My First dataset",
              fill: true,
              borderColor: config.colors.danger,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.danger,
              pointBorderColor: 'rgba(255,255,255,0)',
              pointHoverBackgroundColor: config.colors.danger,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [90, 27, 60, 12, 80],
            }]
          },
          gradientColors: ['rgba(66,134,121,0.15)', 'rgba(66,134,121,0.0)', 'rgba(66,134,121,0)'],
          gradientStops: [1, 0.4, 0],
        },
        blueBarChart: {
          extraOptions: chartConfigs.barChartOptions,
          chartData: {
            labels: ['USA', 'GER', 'AUS', 'UK', 'RO', 'BR'],
            datasets: [{
              label: "Countries",
              fill: true,
              borderColor: config.colors.info,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              data: [53, 20, 10, 80, 100, 45],
            }]
          },
          gradientColors: config.colors.primaryGradient,
          gradientStops: [1, 0.4, 0],
        }
      }
    },
    computed: {
      enableRTL() {
        return this.$route.query.enableRTL;
      },
      isRTL() {
        return this.$rtl.isRTL;
      },
      bigLineChartCategories() {
        return this.$t('dashboard.chartCategories');
      }
    },
    methods: {
      initBigChart(index) {
        let chartData = {
          datasets: [{
            fill: true,
            borderColor: config.colors.primary,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: config.colors.primary,
            pointBorderColor: 'rgba(255,255,255,0)',
            pointHoverBackgroundColor: config.colors.primary,
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: this.bigLineChart.allData[index]
          }],
          labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
        }
        this.$refs.bigChart.updateGradients(chartData);
        this.bigLineChart.chartData = chartData;
        this.bigLineChart.activeIndex = index;
      }
    },
    mounted() {
      this.i18n = this.$i18n;
      if (this.enableRTL) {
        this.i18n.locale = 'ar';
        this.$rtl.enableRTL();
      }
      this.initBigChart(0);
    },
    beforeDestroy() {
      if (this.$rtl.isRTL) {
        this.i18n.locale = 'en';
        this.$rtl.disableRTL();
      }
    }
  };
</script>
<style>

</style>
